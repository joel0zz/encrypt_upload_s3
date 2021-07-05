UI_CONFIG = {
        'description': 'AWS Secret Uploader (KMS)',
        'options': [
        {
            'short_option': '-s',
            'long_option': '--secret',
            'required': True,
            'help': 'The secret that will be encrypted and uploaded.'
        },
            {
                'short_option': '-b',
                'long_option': '--bucket',
                'required': True,
                'help': 'The s3 bucket where the secret will be stored.'
            },
                {
                    'short_option': '-a',
                    'long_option': '--alias',
                    'required': True,
                    'help': 'the KMS alias that will be used to encrypt the file.'
                },
                    {
                        'short_option': '-p',
                        'long_option': '--profile',
                        'required': True,
                        'help': 'the AWS profile in .aws/credential to be used.'
                    },
                        {
                            'short_option': '-n',
                            'long_option': '--name',
                            'required': True,
                            'help': 'the name of the secret to be stored in s3.'
                        }
        ]
}

REGION_NAME = 'ap-southeast-2'