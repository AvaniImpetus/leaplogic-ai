# AWS SQS Utilities

> **Summary:** This module provides helper functions for AWS Simple Queue Service (SQS) operations including sending messages, receiving messages, deleting messages, purging queues, and managing queue URLs. All functions work within the WMG Glue executor context and support optional AWS credentials.

**Common Use Cases:**
- Queue-based job processing and event handling
- Asynchronous message passing between services
- Batch message operations
- Cross-account queue access

---

## Quick Reference

| Task | Function | Example |
|------|----------|---------|
| Send a message | `send_message()` | `send_message(executor, queue_url, {'event': 'signup'})` |
| Read messages | `read_message()` | `read_message(executor, queue_url, max_messages=10)` |
| Delete a message | `delete_message()` | `delete_message(executor, queue_url, receipt_handle)` |
| Purge queue | `purge_queue()` | `purge_queue(executor, queue_url)` |
| Send batch | `send_message_batch()` | `send_message_batch(executor, queue_url, messages_list)` |
| Get queue URL | `get_queue_url()` | `get_queue_url(executor, 'my-queue')` |
| List queues | `get_queue_list()` | `get_queue_list(executor, queue_name_prefix='prod-')` |
| Get queue attributes | `get_queue_attrs()` | `get_queue_attrs(executor, queue_url)` |

---

## Detailed Method Reference

### `read_message()`

**Purpose:** Receive messages from an SQS queue, parse JSON bodies, and optionally delete after reading.

**Parameters:**
- `executor`: Glue executor context
- `queue_url` (str): The URL of the SQS queue
- `max_messages` (int): Maximum messages to receive (1-10, default: 1)
- `wait_time` (int): Long polling wait time in seconds (0-20, default: 0)
- `visibility_timeout` (int): Message visibility timeout in seconds
- `delete_after_read` (bool): Delete messages after reading (default: False)

**Returns:**
```python
{
    'Messages': [
        {
            'MessageId': '...',
            'ReceiptHandle': '...',
            'Body': 'raw body string',
            'ParsedBody': {...} or None,  # JSON parsed if possible
        }
    ],
    'MessageCount': int,
    'Success': True|False
}
```

**Example:**
```python
result = read_message(executor, queue_url, max_messages=5, delete_after_read=True)
for msg in result['Messages']:
    print(msg['ParsedBody'])  # Use parsed JSON
```

---

### `send_message()`

**Purpose:** Send a single message to an SQS queue. Supports FIFO queue parameters.

**Parameters:**
- `executor`: Glue executor context
- `queue_url` (str): The URL of the SQS queue
- `message_body` (str or dict): Message body (dicts are JSON-encoded automatically)
- `delay_seconds` (int): Delay before message is available (0-900)
- `message_group_id` (str): For FIFO queues
- `message_deduplication_id` (str): For FIFO queues

**Example:**
```python
send_message(executor, queue_url, {'event': 'user_signup', 'user_id': 123})
```

---

### `send_message_batch()`

**Purpose:** Send multiple messages in batches of 10 (SQS API limit).

**Parameters:**
- `messages` (list): List of message dicts with `Id` and `MessageBody`

**Example:**
```python
batch = [
    {'Id': '1', 'MessageBody': {'event': 'a'}},
    {'Id': '2', 'MessageBody': 'plain text'}
]
send_message_batch(executor, queue_url, batch)
```

---

### `delete_message()`

**Purpose:** Delete a single message using its receipt handle.

**Example:**
```python
delete_message(executor, queue_url, receipt_handle)
```

---

### `purge_queue()`

**Purpose:** Remove all messages from a queue. AWS may take up to 60 seconds to complete.

**Warning:** Destructive operation. Cannot purge more than once per 60 seconds.

**Example:**
```python
purge_queue(executor, queue_url)
```

---

### `get_queue_url()`

**Purpose:** Resolve a queue name to its full URL.

**Example:**
```python
result = get_queue_url(executor, 'my-queue-name')
queue_url = result['QueueUrl']
```

---

### `get_queue_list()`

**Purpose:** List queues in the account, optionally filtered by name prefix.

**Example:**
```python
queues = get_queue_list(executor, queue_name_prefix='prod-')
for q in queues['Queues']:
    print(q['QueueName'], q['QueueUrl'])
```

---

## Error Handling

All functions return a dict with `Success` flag:
```python
result = send_message(executor, queue_url, data)
if not result['Success']:
    print(f"Error: {result['Error']}")
```

Common errors:
- `NoCredentialsError`: AWS credentials not configured
- `ClientError`: AWS service error (check `result['Error']`)