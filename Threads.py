import threading as _


class Conta(object):

    def __init__(self, nome=None, saldo=0):
        self.saldo = saldo
        self.cliente = nome

    def get_saldo(self):
        return self.saldo

    def get_nome(self):
        return self.cliente

    def transfere(self, conta, transferencia, protect):
        protect.acquire()
        try:
            if self.saldo >= transferencia:
                conta.saldo += transferencia
                self.saldo -= transferencia
                print(self.get_nome(), 'tem', self.get_saldo())
                print(conta.get_nome(), 'tem', conta.get_saldo())
        finally:
            protect.release()

if __name__ == '__main__':
    joao = Conta('Joao Pedro Felipe', 10000)
    claudia = Conta('Claudia Nascimento Souza', 0)

    num_tread = 100

    thrs = [ ]

    lock = _.Lock()

    for threads in range(num_tread):
        thread = _.Thread(target=joao.transfere, args=(claudia, 1, lock))
        thread.start()
        thread = _.Thread(target=claudia.transfere, args=(joao, 1, lock))
        thread.start()

