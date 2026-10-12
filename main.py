# finding art club members
from pyscript import display, document


def name_finder(e):
    document.getElementById('result').innerHTML = ' '
    first_name = document.getElementById('firstname').value.lower().strip()
    last_name = document.getElementById('surname').value.lower().strip() 
    artclub_members = ['jaena' +'ambata', 'frances'+'torculas', 'zoe'+'bueno', 'jack'+'penas' , 'yanna'+'de la cruz', 'marcus'+'viray']
    artclub_members = first_name + last_name in artclub_members

    display_message = (f'Sorry, no {first_name} {last_name} in the art club', f'Congratulations {first_name} {last_name} is now an art club member!')
    
    
    display(display_message[artclub_members], target='result')