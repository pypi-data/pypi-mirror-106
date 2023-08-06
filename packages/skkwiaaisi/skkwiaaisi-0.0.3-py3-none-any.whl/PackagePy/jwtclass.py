import jwt
from datetime import datetime, timedelta

class Token:
    
    def jwt_encode(self, firstclasscode, machineid):
        SECRET_KEY = 'lcms'        
        encoded = jwt.encode({'exp':datetime.utcnow() + timedelta(seconds=1800),'firstClassCode' : firstclasscode, 'machineId' : machineid}, SECRET_KEY, algorithm = 'HS256')
        encoded_string = str(encoded.decode('utf-8'))
        result = {"resultCode":"S", "accesstoken":encoded_string}
        return result, 200 

    def jwt_decode(self, accesstoken):
        SECRET_KEY = 'lcms'
        jwt.decode(accesstoken, SECRET_KEY, algorithm = 'HS256')
        try:
            return True
        except jwt.ExpiredSignatureError:
            return {'message': 'EXPIRED_TOKEN'}, 400
