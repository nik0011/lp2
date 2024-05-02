public class StringBitwiseOperations {

    public static void main(String[] args) {
        String str = "Hello World";

        System.out.println("Original String: " + str);

        System.out.println("\nCharacter\tAND\tOR\tXOR");
        for (char c : str.toCharArray()) {
            int andResult = c & 127;
            int orResult = c | 127;
            int xorResult = c ^ 127;

            System.out.println(c + "\t\t" + andResult + "\t" + orResult + "\t" + xorResult);
        }
    }
}