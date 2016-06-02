import macros

####list_of_vehicle
### add time_incre at the end of this function


def phase_change(intersection):
    if intersection.action == 1:
        if intersection.current_phase + 1 > macros.NSRED_EWYELLOW:
            intersection.current_phase = macros.NSGREEN_EWRED

        else:
            intersection.current_phase = intersection.current_phase + 1
        intersection.action = 0


def process_one_lane(current_lane, current_inter, cars_list, signal):
    '''
    process one lane, given the signal
    '''

    current_car = cars_list

    if signal == macros.NSGREEN_EWRED:
        while current_car:
            check_turn_and_change_lane(current_lane, current_inter, current_car)
            i = [macros.WESTL, macros.EASTL, macros.NORTHL, macros.SOUTHL,
                 macros.WESTR, macros.EASTR, macros.NORTHR, macros.SOUTHR].index(current_lane)
            side_lane = [macros.WESTR, macros.EASTR, macros.NORTHR, macros.SOUTHR,
                         macros.WESTL, macros.EASTL, macros.NORTHL, macros.SOUTHL][i]
            change_lane()
            if not current_car.prev:
                if current_car.speed < macros.CRUISE_SPEED:
                    current_car.acc = macros.ACCELERATION
                else:
                    current_car.speed = macros.CRUISE_SPEED
                    current_car.acc = 0
            else:
                if (current_car.prev.location - current_car.location) < macros.SAFE_DIST:
                    current_car.acc = macros.DECELERATION
                elif (current_car.prev.location - current_car.location) == macros.SAFE_DIST:
                    current_car.acc = 0
                else:
                    if current_car.speed < macros.CRUISE_SPEED:
                        current_car.acc = macros.ACCELERATION
                    else:
                        current_car.speed = macros.CRUISE_SPEED
                        current_car.acc = 0

            current_car = current_car.next


def check_turn_and_change_lane(current_lane, current_inter, current_car):
    '''
    check turn and change lane action for current_car given current lane and current intersection
    '''

    if current_inter == current_car.my_path[-1]:    # already at destination
        if current_lane == macros.WESTL:
            if current_car.final_dir == macros.SOUTH:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif current_car.final_dir == macros.NORTH:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.WESTR:
            if current_car.final_dir == macros.SOUTH:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif current_car.final_dir == macros.NORTH:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.NORTHL:
            if current_car.final_dir == macros.WEST:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif current_car.final_dir == macros.EAST:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.NORTHR:
            if current_car.final_dir == macros.WEST:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif current_car.final_dir == macros.EAST:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.EASTL:
            if current_car.final_dir == macros.NORTH:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif current_car.final_dir == macros.SOUTH:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.EASTR:
            if current_car.final_dir == macros.NORTH:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif current_car.final_dir == macros.SOUTH:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.SOUTHL:
            if current_car.final_dir == macros.EAST:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif current_car.final_dir == macros.WEST:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
        elif current_lane == macros.SOUTHR:
            if current_car.final_dir == macros.EAST:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif current_car.final_dir == macros.WEST:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            else:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0

    else:
        for i in range(0, len(current_car.my_path)-1):  #decide if
            if current_inter == current_car.my_path[i]:
                next_inter = current_car.my_path[i+1]
                break
            else:
                print("A car is not on its path!!!!!!")
                return -1

        if current_lane == macros.WESTL:
            if next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif next_inter[0] == current_inter[0]-1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            elif next_inter[1] == current_inter[1]+1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.WESTR:
            if next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif next_inter[0] == current_inter[0]-1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            elif next_inter[1] == current_inter[1]+1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.NORTHL:
            if next_inter[1] == current_inter[1]-1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif next_inter[1] == current_inter[1]+1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            elif next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.NORTHR:
            if next_inter[1] == current_inter[1]-1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif next_inter[1] == current_inter[1]+1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            elif next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.EASTL:
            if next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif next_inter[0] == current_inter[0]-1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            elif next_inter[1] == current_inter[1]-1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.EASTR:
            if next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif next_inter[0] == current_inter[0]-1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            elif next_inter[1] == current_inter[1]-1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.SOUTHL:
            if next_inter[1] == current_inter[1]+1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 1
            elif next_inter[1] == current_inter[1]-1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 0
            elif next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
        elif current_lane == macros.SOUTHR:
            if next_inter[1] == current_inter[1]-1:
                current_car.turn = macros.RIGHT
                current_car.change_lane = 0
            elif next_inter[1] == current_inter[1]+1:
                current_car.turn = macros.LEFT
                current_car.change_lane = 1
            elif next_inter[0] == current_inter[0]+1:
                current_car.turn = macros.STRAIGHT
                current_car.change_lane = 0
            else:
                print("You cannot make a U turn!!!!!!!")
                return -1
    return


def change_lane(side_lane, car):
    ##1 means turn left
    find_lagging_car = 0
    current_side_lane_car = side_lane
    while current_side_lane_car:
        if current_side_lane_car.position < car.position:
            find_lagging_car = 1
            lagging_car = current_side_lane_car
            if current_side_lane_car.prev:
                leading_car = current_side_lane_car.prev
                if (leading_car.position - lagging_car.position)/car.speed > macros.CRITICAL_GAP:
                    car.prev.next = car.next
                    car.next.prev = car.prev
                    car.next = lagging_car
                    lagging_car.prev = car
                    car.prev = leading_car
                    leading_car.next = car
                else:
                    car.acc = macros.DECELERATION
            else:
                current_side_lane_car.prev = car
                car.prev.next = car.next
                car.next.prev = car.prev
                car.next = current_side_lane_car
            break
        if not current_side_lane_car.next:
            break
        current_side_lane_car = current_side_lane_car.next


    if find_lagging_car == 0:
        car.prev.next = car.next
        car.next.prev = car.prev
        car.prev = current_side_lane_car







def intersection_process(intersection,action,):
    phase_change(intersection,action)