class PayPalGateway:
    def process_payment(self, amount):
        return f"Transaction of amount ${amount} processed through payPal"


class StripeGateway:
    def pay(self, amount):
        return f"Transaction of amount ${amount} processed through stripe"


class CryptoGateway:
    def make_payment(self, amount):
        return f"Transaction of amount ${amount} processed through crypto (Bitcoin)"


class PaymentFacade:
    def __init__(self) -> None:
        self._paypal = PayPalGateway()
        self._stripe = StripeGateway()
        self._crypto = CryptoGateway()
    
    def process_payment(self, amount, gateway):
        if gateway == 'paypal':
            return self._paypal.process_payment(amount)
        elif gateway == 'crypto':
            return self._crypto.make_payment(amount)
        elif gateway == 'stripe':
            return self._stripe.pay(amount)
        else:
            return 'Invalid gateway selection'

if __name__ == '__main__':
    # Creating PaymentFacade instance
    payment_facade = PaymentFacade()

    print(payment_facade.process_payment(100, 'paypal'))
    print(payment_facade.process_payment(150, 'stripe'))
    print(payment_facade.process_payment(200, 'crypto'))
    print(payment_facade.process_payment(300, 'invalid_gateway'))

