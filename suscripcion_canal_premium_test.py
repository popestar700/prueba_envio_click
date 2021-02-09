import unittest
import json

clients = json.loads(open('clientes.json').read())

def search_client(email_user):
    for a in clients:
        if a['email'] == email_user:
            return a['email']
    return 'The client doesn´t exit'

def verified_subscribe_cliente(email_user):
    for a in clients:
        if a['email'] == email_user:
            return a['vip']


def channel_exit(channel_exit):
    channels_dict = json.loads(open('canales.json').read())

    channels_keys = list(channels_dict.keys())
    for channel in channels_keys:
        if channel == channel_exit:
            return True
    return False

def susbcripcion_channel(channel, period_time):
    if isinstance(period_time, int):
        #verify if channel exit
        if channel_exit(channel):
            if period_time <= 12:
                print('The subscription channel was succesfully')
                return True
            else:
                print('The subscription to the channel must be from 1 to 12 months')
                return False
        else:
            print('The channel doesn´t exists')
            return False
    else:
        return False


class SuscripcionCanalPremiumTest(unittest.TestCase):
    
    def test_suscripcion_canal_premium(self):
        #test if client susbcribe a channel
        self.assertEqual(verified_subscribe_cliente('gortiz0@mapy.cz'), False)
        self.assertEqual(verified_subscribe_cliente('mrice6@geocities.jp'), False)

    
    def test_client_exit(self):
        #test if email user exit
        self.assertEqual(search_client('ralvarez9@nsw.gov.au'), 'ralvarez9@nsw.gov.au')
        self.assertEqual(search_client('jlmytef21@gmail.com'), 'ralvarez9@nsw.gov.au')
    
    def test_channel_exit(self):
        #test if channel exits
        self.assertTrue(channel_exit('W'), 'The channel doesn´t exits')

    def test_susbcripcion_channel(self):
        #test susbcribe client a channel
        self.assertTrue(susbcripcion_channel('W', 10))


if __name__ == "__main__":
    unittest.main()