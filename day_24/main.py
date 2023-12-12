PLACEHOLDER = "[name]"


def get_names():
    with open("./input/names/invited_names.txt") as names:
        name_list = []
        for name in names.readlines():
            name_list.append(name.strip())
        return name_list


def personalize_invitation(receiver_name):
    with open("./input/letters/starting_letter.txt") as template:
        content = template.read()
        return content.replace(PLACEHOLDER, receiver_name)


invited_guests = get_names()

for guest in invited_guests:
    invitation = personalize_invitation(receiver_name=guest)
    with open(f"./output/ready_to_send/letter_for_{guest}.txt", mode="w") as invite:
        invite.write(invitation)
