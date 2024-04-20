class Contato:

    def __init__(self, telefone, email, instagram=None, facebook=None, twitter=None, whatsapp=None):
        self.telefone = telefone
        self.email = email
        self.instagram = instagram
        self.facebook = facebook
        self.twitter = twitter
        self.whatsapp = whatsapp

    def to_json(self):
        return {
            'telefone': self.telefone,
            'email': self.email,
            'instagram': self.instagram,
            'facebook': self.facebook,
            'twitter': self.twitter,
            'whatsapp': self.whatsapp
        }