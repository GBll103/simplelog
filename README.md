# simplelog
A log module made by Python

## BEFORE WE BEGIN
Define a *log_obj()* object

**Example:**
```python
import logs
logger = logs.log_obj()
```

## LOG OUTPUT MODE
Change the Boolean value of “isWritingInFile” to switch the output mode (True outputs to the console; False outputs to a file).

**Example:**

File mode:
```python
logger.isWritinginFile=True # This will write the log to a file.
```

Console Mode:
```python
logger.isWritinginFile=False # This will write the log to console.
```

## OUTPUT LOG

Call the “log” function to output a log message.

```python
logger.log(MESSAGE,FROMWHERE,MESSAGETYPE)
# OUTPUT: [{LOGTIME}] [{MESSAGETYPE}] [FROM:{FROMWHERE}] MESSAGE
```
**Example:**
```python
logger.log("testMes","MAIN","INFO")
# OUTPUT: [nowtime] [INFO] [FROM:MAIN] testMes
```

