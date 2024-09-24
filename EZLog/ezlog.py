import os
from datetime import datetime
import pytz

class EZ:
    logDirPath: str = os.path.abspath("./_EZLOG_")

    @classmethod
    def log(cls, detailedMsg: str, selfDefinedCode: int = 0, selfDefinedTag: str = 'INFO') -> tuple[bool, str]:
        now = datetime.now()
        try:
            if not os.path.exists(cls.logDirPath):
                os.makedirs(cls.logDirPath)
            logMessage = f"[{selfDefinedCode}：{selfDefinedTag}]\n{detailedMsg}\n== {now.strftime('%Y/%m/%dT%H:%M:%S.%f')} (UTC：{now.astimezone(pytz.utc).strftime('%Y/%m/%dT%H:%M:%S.%f')}) ==\n"
            logFilePath = os.path.abspath(f'{cls.logDirPath}/{now.strftime("%Y%m%d")}_log.txt')
            with open(logFilePath, "a", encoding='utf-8') as logFile:
                logFile.write(logMessage)
            return True, cls.logDirPath
        except Exception as ex:
            print(f'{cls.logDirPath}')
            print('[EZLog] log failed.\n')
            print(str(ex))
            return False, cls.logDirPath
