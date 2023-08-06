import platform,socket,logging,psutil,re,uuid
class Sys:
    def __init__(self):
        self.info={}	
        self.info['machine']=platform.machine()		
        self.info['version']=platform.version()
        self.info['platform']=platform.platform()
        self.info['uname']=platform.uname()
        self.info['system']=platform.system()
        self.info['processor']=platform.processor()
        self.info['hostname']=socket.gethostname()
        self.info['iP-Address']=socket.gethostbyname(socket.gethostname())
        self.info['MAC-Address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        self.info['RAM']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        
    def get_info(self):
        return self.info