import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Battleship {
    public static void main(String[] args) {
        Player player1 = new Player("Player 1");
        Player player2 = new Player("Player 2");
        Board board1 = new Board();
        Board board2 = new Board();

        player1.setBoard(board1);
        player2.setBoard(board2);

        System.out.println(player1.getName() + ", place your ships:");
        player1.placeShips();
        System.out.println(player2.getName() + ", place your ships:");
        player2.placeShips();

        boolean gameOver = false;
        Player currentPlayer = player1;
        Player opponentPlayer = player2;

        while (!gameOver) {
            System.out.println(currentPlayer.getName() + "'s turn:");
            currentPlayer.attack(opponentPlayer);
            gameOver = opponentPlayer.getBoard().checkVictory();

            System.out.println("Current Board of " + opponentPlayer.getName() + ":");
            opponentPlayer.getBoard().printBoard(false);
            System.out.println("Current Board of " + currentPlayer.getName() + ":");
            currentPlayer.getBoard().printBoard(true);

            if (!gameOver) {
                Player temp = currentPlayer;
                currentPlayer = opponentPlayer;
                opponentPlayer = temp;
            }
        }

        System.out.println(currentPlayer.getName() + " wins!");
    }
}

class Player {
    private String name;
    private Board board;
    private Scanner scanner;

    public Player(String name) {
        this.name = name;
        this.scanner = new Scanner(System.in);
    }

    public String getName() {
        return name;
    }

    public void setBoard(Board board) {
        this.board = board;
    }

    public Board getBoard() {
        return board;
    }

    public void placeShips() {
        int[] shipSizes = {5, 4, 3, 3, 2};

        for (int size : shipSizes) {
            boolean placed = false;
            while (!placed) {
                System.out.println("Enter the starting coordinates (x y) and orientation (h/v) for a ship of size " + size + ": ");
                int x = scanner.nextInt();
                int y = scanner.nextInt();
                char orientation = scanner.next().charAt(0);

                Ship ship = new Ship(size);
                placed = board.placeShip(ship, x, y, orientation);
                if (!placed) {
                    System.out.println("Invalid position. Try again.");
                }
            }
            board.printBoard(true);
        }
    }

    public void attack(Player opponent) {
        boolean validAttack = false;
        while (!validAttack) {
            System.out.println("Enter coordinates (x y) to attack: ");
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            validAttack = opponent.getBoard().receiveAttack(x, y);
            if (validAttack) {
                System.out.println("Hit!");
            } else {
                System.out.println("Miss!");
            }
        }
    }
}

class Board {
    private char[][] grid;
    private List<Ship> ships;

    public Board() {
        grid = new char[10][10];
        ships = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                grid[i][j] = '-';
            }
        }
    }

    public boolean placeShip(Ship ship, int x, int y, char orientation) {
        List<int[]> positions = new ArrayList<>();
        for (int i = 0; i < ship.getSize(); i++) {
            if (orientation == 'h') {
                if (x + i >= 10 || grid[y][x + i] != '-') {
                    return false;
                }
                positions.add(new int[]{x + i, y});
            } else if (orientation == 'v') {
                if (y + i >= 10 || grid[y + i][x] != '-') {
                    return false;
                }
                positions.add(new int[]{x, y + i});
            } else {
                return false;
            }
        }
        for (int[] pos : positions) {
            grid[pos[1]][pos[0]] = 'S';
        }
        ship.setPositions(positions);
        ships.add(ship);
        return true;
    }

    public boolean receiveAttack(int x, int y) {
        for (Ship ship : ships) {
            if (ship.isHit(x, y)) {
                grid[y][x] = 'X';
                return true;
            }
        }
        grid[y][x] = 'O';
        return false;
    }

    public boolean checkVictory() {
        for (Ship ship : ships) {
            if (!ship.isSunk()) {
                return false;
            }
        }
        return true;
    }

    public void printBoard(boolean showShips) {
        System.out.print("  ");
        for (int i = 0; i < 10; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
        for (int i = 0; i < 10; i++) {
            System.out.print(i + " ");
            for (int j = 0; j < 10; j++) {
                if (showShips) {
                    System.out.print(grid[i][j] + " ");
                } else {
                    if (grid[i][j] == 'S') {
                        System.out.print("- ");
                    } else {
                        System.out.print(grid[i][j] + " ");
                    }
                }
            }
            System.out.println();
        }
    }
}

class Ship {
    private int size;
    private List<int[]> positions;
    private int hits;

    public Ship(int size) {
        this.size = size;
        this.positions = new ArrayList<>();
        this.hits = 0;
    }

    public int getSize() {
        return size;
    }

    public void setPositions(List<int[]> positions) {
        this.positions = positions;
    }

    public boolean isHit(int x, int y) {
        for (int[] position : positions) {
            if (position[0] == x && position[1] == y) {
                hits++;
                return true;
            }
        }
        return false;
    }

    public boolean isSunk() {
        return hits >= size;
    }
}