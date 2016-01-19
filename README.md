# Septime availability checker

http://www.tripadvisor.co.uk/Restaurant_Review-g187147-d2185868-Reviews-Septime-Paris_Ile_de_France.html

        [th0m@th0m-ks septime]$ crontab -l
        * * * * *  ~/septime/check_resa.py | mail -E -s 'Septime' me@domain.fr
