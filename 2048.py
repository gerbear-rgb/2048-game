#import all the logic we made in logic.py file 
import logic

if __name__ == '__main__':
    mat = logic.start_game()
    
while True:
    usr_input = input('Press the command: ')
    
    if usr_input in ['W', 'w']:
        
        mat, flag = logic.move_up(mat)
        
        status = logic.get_current_state(mat)
        print(status)
        
        if status == 'GAME NOT OVER':
            logic.add_new_2(mat)

        else:
            break

    elif usr_input in ['S', 's']:
        
        mat, flag = logic.move_down(mat)
        status = logic.get_current_state(mat)
        
        if status == 'GAME NOT OVER':
            logic.add_new_2(mat)

        else:
            break

    elif usr_input in ['A', 'a']:
        mat, flag = logic.move_left(mat)
        status = logic.get_current_state(mat)
        if status == 'GAME NOT OVER':
            logic.add_new_2(mat)
        else:
            break

    elif usr_input in ['D', 'd']:
        mat, flag = logic.move_right(mat)
        status = logic.get_current_state(mat)
        if status == 'GAME NOT OVER':
            logic.add_new_2(mat)
        else:
            break

    else:
        print('Invalid Key Pressed')
        
    for i in range(4):
        print(mat[i])
