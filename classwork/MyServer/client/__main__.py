import argparse
import requests

parser = argparse.ArgumentParser(
            prog='client',
            description='Send and receives messages',
            epilog='I hope you to be happy')

parser.add_argument('subcommand', action='store',
                    help='subcommand to execute')

parser.add_argument('-q', '--quantity', action='store_const',
                    const='quant', dest='info',
                    help='quantity of clients on server')

parser.add_argument('-l', '--list', action='store_const',
                    const='list', dest='info',
                    help='list of clients on server')

parser.add_argument('-m', '--messages', action='store_const',
                    const='mesg', dest='info',
                    help='number of messages on server')

parser.add_argument('-c', '--client', action='store',
                    type=int, default=None,
                    dest='client_id',
                    help='client ID')

parser.add_argument('-C', '--count', action='store_const',
                    const='count', dest='query',
                    help='Quantity of messages for client')

parser.add_argument('-g', '--get', action='store_const',
                    const='get', dest='query',
                    help='Get next message for client')

parser.add_argument('-M', '--message', action='store', type=str,
                    dest='message',
                    help='Message to send')

args = parser.parse_args()

match args.subcommand:
    case 'info':
        match args.info:
            case 'quant':
                recv = requests.get('http://localhost:8000/clients/quantity')
                print(recv.text)
            case 'list':
                recv = requests.get('http://localhost:8000/clients/list')
                print(recv.text)
            case 'mesg':
                recv = requests.get('http://localhost:8000/clients/message')
                print(recv.text)
            case _:
                print('Invalid option')
    case 'recv':
        match args.query:
            case 'get':
                recv = requests.get(f'http://localhost:8000/next/{args.client_id}')
                print(recv.text)
            case 'count':
                recv = requests.get(f'http://localhost:8000/number/{args.client_id}')
                print(recv.text)
            case _:
                print('Invalid option')
    case 'send':
        recv = requests.post(f'http://localhost:8000/message_to/{args.client_id}',
                             data=args.message.encode('utf-8'))
        print(recv.text)
    case _:
        print('Invalid subcommand: ', args.subcommand)

#    http://host:8000/clients/quantity -> GET
#    http://host:8000/message_to/234  -> POST
#    http://host:8000/number/234 -> GET
#    http://host:8000/next/234 -> GET
#    http://host:8000/clients/list -> GET
#    http://host:8000/clients/message -> GET

