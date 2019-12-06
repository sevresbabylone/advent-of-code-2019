package adventofcode;

import java.util.ArrayList;


public class Day004 {
    public static ArrayList<String> getAllPasswords(int lowerBound, int upperBound) {
        ArrayList<String> passwords = new ArrayList<String>();
        for (int i = lowerBound; i <= upperBound; i++) {
            String password = String.valueOf(i);
            if (checkAdjDigits(password) && alwaysAscending(password)) {
                passwords.add(password);
            }
        }
        return passwords;
    }
    public static Boolean checkAdjDigits(String s) {
        char prev = '0';
        for(char curr : s.toCharArray()) {
            if (curr == prev) return true;
            prev = curr;
        }
        return false;
    }
    public static Boolean alwaysAscending(String s) {
        int highest = 0;
        for (char curr : s.toCharArray()) {
            int currentValue = Character.getNumericValue(curr);
            if (currentValue < highest) return false;
            else highest = currentValue;
        }
        return true;
    }
    public static void main(String[] args) {
        String[] puzzleInput = "128392-643281".split("-");
        ArrayList<String> passwords = getAllPasswords(Integer.parseInt(puzzleInput[0]), Integer.parseInt(puzzleInput[1]));

        System.out.println(passwords.size());

    }
}
