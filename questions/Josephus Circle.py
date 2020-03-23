# Josephus circle
#
# N people have decided to elect a leader by arranging themselves in a circle and
# eliminating every Mth person around the circle, closing ranks as each person drops out.
# Find the last one remaining.


def jos_circle(n, k):
    if n == 1:
        return 1
    else:
        return (jos_circle(n - 1, k) + k-1) % n + 1


print("The chosen leader is no.", jos_circle(7, 3))
