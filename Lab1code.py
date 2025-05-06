
def vote_menu():
    print('-'*34)
    print('VOTE MENU')
    print('-' * 34)
    print('v: Vote')
    print('x: Exit')
    user_choice = input('Option: ').strip().lower()
    while user_choice != 'v' and user_choice != 'x':
        user_choice = input('Invalid (v/x): ').strip().lower()
    return user_choice

def candidate_menu():
    print('-' * 34)
    print('1: Bianca')
    print('2: Edward')
    print('3: Felicia')
    user_vote = input('Candidate: ').strip()
    while user_vote != '1'and user_vote != '2' and user_vote != '3':
        user_vote = input('Invalid (1/2/3): ').strip()
    return user_vote

def main(menu_vote, candidate_vote):
    bianca = 0
    edward = 0
    felicia = 0
    while menu_vote != 'x':
        menu_vote = vote_menu()
        if menu_vote == 'x':
            break
        candidate_vote =  candidate_menu()
        if candidate_vote == '1':
            print('Voted Bianca')
            bianca+=1
        elif candidate_vote == '2':
            print('Voted Edward')
            edward+=1
        elif candidate_vote == '3':
            print('Voted Felicia')
            felicia+=1
    print('-' * 57)
    print(f'Bianca - {bianca}, Edward - {edward}, Felicia - {felicia}, Total - {bianca + edward + felicia}')
    print('-' * 57)

main(0,0)