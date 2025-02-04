import math, sqlite3, time

def X(a, b):
    return A*(a**4 + -6*a**2*b**2 + b**4) + B*(a**3 - 3*a*b**2) + C*(a**2 - b**2) + D*a + E

def Y(a, b):
    return A*(4*a**3*b - 4*a*b**3) + B*(3*a**2*b - b**3) + C*(2*a*b) + D*b


def Proximity(a, b):
    return X(a, b)**2 + Y(a, b)**2

def OneDigitAtATime(cx, cy, decimal_place):
    Dict = {}
    Relevance = []
    for i in range(-5, 6):
        y_change = round(i/(10**decimal_place), decimal_place)
        for j in range(-5, 6):
            x_change = round(j/(10**decimal_place), decimal_place)
            inst_x, inst_y = round(cx + x_change, decimal_place), round(cy + y_change, decimal_place)
            Dict[Proximity(inst_x, inst_y)] = (inst_x, inst_y) # ties values to their proximity
            Relevance.append(Proximity(inst_x, inst_y))
    Relevance.sort() # makes a list of all guesses and sorts them
    return Dict[Relevance[0]]

global A, B, C, D, E
start_time = time.time()
conn = sqlite3.connect("QuarticPolies.db")

# making and populating the tables
if conn:

    cursor = conn.cursor()
    command = """CREATE TABLE IF NOT EXISTS POLIES (
    A integer NOT NULL,
    B integer NOT NULL,
    C integer NOT NULL,
    D integer NOT NULL,
    E integer NOT NULL,
    PART1 float NOT NULL,
    PART2 float NOT NULL,
    PART3 float NOT NULL,
    PART4 float NOT NULL
);"""

    try:
        cursor.execute(command)
    except:
        print("That didn't work :(")

    width = 3 # 299
    upper, lower = int((width + 1)/2), -int((width - 1)/2)
    for A in range(lower, upper):
        print(A)
        if A != 0:
            for B in range(lower, upper):
                for C in range(lower, upper):
                    for D in range(lower, upper):
                        for E in range(lower, upper):
                            cx, cy = 0, 0
                            for i in range(5):
                                cx, cy = OneDigitAtATime(cx, cy, i)
                            c2x = round(-B/2/A - cx, 4)
                            if E == 0 and (cx**2 + cy**2) == 0:
                                c2y = round(abs(c2x), 4)
                            else:
                                c2y = abs(E/A/(cx**2 + cy**2) - c2x**2)
                                c2y = round(math.sqrt(c2y), 4)

                            command_populate = "INSERT INTO POLIES VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
                            data = (A, B, C, D, E, cx, cy, c2x, c2y)
                            conn.executemany(command_populate, [data])
                            conn.commit()
    conn.close()
end_time = time.time()
elapsed_time = end_time - start_time
No_of_polies = width**5 - width**4
print(f"{No_of_polies} Quartic Polynomials added to database")
print(f"{round(No_of_polies/elapsed_time, 4)} Polies added per second")


