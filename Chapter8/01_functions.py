def percentage(marks):
    p= ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks = [79, 82, 95, 65]
percent = percentage(marks)
print(percent)