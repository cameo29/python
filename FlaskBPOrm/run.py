'''
Created on 2017. 11. 8.
시작점
'''
from service import create_app

application = create_app()

if __name__=='__main__':
    print("running server...")
    application.run(host='0.0.0.0', port=3000, debug=True)
