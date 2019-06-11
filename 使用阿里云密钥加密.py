from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkkms.request.v20160120 import EncryptRequest
from aliyunsdkkms.request.v20160120 import DecryptRequest

client = AcsClient('LT****pY', 'cQ*************1', 'cn-hangzhou')
a=EncryptRequest.EncryptRequest()
a.set_Plaintext('dGVzdDEyMw==')
a.set_KeyId('56************c977')
response = client.do_action_with_exception(a)
print response


print '************'b=DecryptRequest.DecryptRequest()
b.set_CiphertextBlob('M2NlMDlmODUtMTRjNy00MjQwLWEwYzgtYWVmMWFkNmVjZGZhdjVORjluZTUzOSs5dG8wbjdBWFp2NHZ5WXJqSGhrTFRBQUFBQUFBQUFBQ0k1aVpqb3NScUVZa0x4S0E5eDFDZ3dCb0V1dHZPZXBDblhTVU4=')
response = client.do_action_with_exception(b)
print response
