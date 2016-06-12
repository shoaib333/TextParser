class grammar:
    def __init__(self):
        self.grammar = { 'atfMessages' : ['AtfMessages', 'AtfPortChecker', 'AtfPriorityQueue', 'AtfAtMmiTranslation',
                                            'AtfExceptionHandler' ,'AtfSocketTestManager', 'AtfL1TestSystemServer',
                                            'AtfTargetSocketServer', 'AtfCBSPlatformInterface',
                                            'AtfCBSPlatformInterface', 'AtfL1TestHarnessSuiteServer'],
                        'RunCmd'       : ['Number','tracecap','testserver.exe','taskkill','tasklist'],
                        'cmw'          : ['cmwsoap', 'cmwxmlrpcclient'],
                        'misc'         : ['artefact','commonlib','fixsuds','logger_base' ,'wireshark','helperFunctions'],
                        'explorer'     : ['peexplorer', 'xddexplorer'],
                        'atmmi'        : ['atmmimanager', 'atmmihandlers'],
                        'type'         : ['INFO', 'DEBUG', 'WARNING']
                       }


# class grammar:
#     def __init__(self):
#         self.p_messageType = ['retry']
#         self.p_atfMessages = ['AtfMessages', 'AtfPortChecker', 'AtfPriorityQueue', 'AtfAtMmiTranslation', 'AtfExceptionHandler'
#                          ,'AtfSocketTestManager', 'AtfL1TestSystemServer', 'AtfTargetSocketServer', 'AtfCBSPlatformInterface'
#                          ,'AtfCBSPlatformInterface', 'AtfL1TestHarnessSuiteServer']
#
#         #RunCmd[tasklist](126) #RunCmd(126) #RunCmd[tracecap](126) #RunCmd[taskkill](126) #RunCmd[tasklist](126) #RunCmd[testserver.exe](126)
#         self.p_RunCmd = ['RunCmd','Number','tracecap','testserver.exe','taskkill','tasklist']
#
#         self.p_cmw = ['cmwsoap', 'cmwxmlrpcclient']
#
#         self.p_cmw_messageInfoType = ['CMW Test status'] #RUNNING #TODO:check other values in cmw tests
#
#         #artefact(125)                :  :+= testServer.trace => test_framework
#         #when messageType is arteface then parse messageInfo type with :+= and hard code as artefact type
#         self.p_misc= ['artefact','fixsuds', 'wireshark','helperFunctions']
#
#         #commonlib(38)                :  :selected parameter key is now = ['PWR_LVL_HIGH']
#         #TODO: when message type is commonlib no messageInfo tag is offered, hard code as commonlib
#         self.p_commonlib = ['commonlib']
#         self.p_explorer = ['peexplorer', 'xddexplorer']
#         self.p_loggerbase = ['logger_base']
#         self.p_atmmi = ['atmmimanager', 'atmmihandlers']
#         self.p_type = ['INFO', 'DEBUG', 'WARNING']

