# Septime availability checker

        [th0m@th0m-ks septime]$ crontab -l
        * * * * *  ~/septime/check_resa.py | mail -E -s 'Septime' me@domain.fr
