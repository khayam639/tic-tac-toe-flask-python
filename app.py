from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize the board (3x3)
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    # Check tie
    if all(cell != "" for row in board for cell in row):
        return "Tie"
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    global current_player, board
    winner = check_winner()

    if request.method == "POST":
        row = int(request.form["row"])
        col = int(request.form["col"])
        if board[row][col] == "" and winner is None:
            board[row][col] = current_player
            current_player = "O" if current_player == "X" else "X"
        return redirect(url_for("index"))

    return render_template("index.html", board=board, winner=winner, player=current_player)

@app.route("/reset")
def reset():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
