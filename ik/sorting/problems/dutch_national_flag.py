def dutch_flag_sort(balls):
    green_start = 0
    right = len(balls) - 1
    left = 0

    while left <= right:
        ball = balls[left]
        if ball == "R":
            balls[green_start], balls[left] = balls[left], balls[green_start]
            green_start += 1
            left += 1
        elif ball == "B":
            balls[left], balls[right] = balls[right], balls[left]
            right -= 1
        else:
            left += 1

    return balls


if __name__ == '__main__':
    print(dutch_flag_sort(balls=["G", "B", "G", "G", "R", "B", "R", "G"]))  # ["R", "R", "G", "G", "G", "G", "B", "B"]
    print(dutch_flag_sort(balls=["G", "B", "G", "G", "R", "B", "R", "G"]))  # ["R", "R", "G", "G", "G", "G", "B", "B"]
