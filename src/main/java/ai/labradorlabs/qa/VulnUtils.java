package ai.labradorlabs.qa;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class VulnUtils {

    public static String insecureHash(String password) throws Exception {
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] digest = md.digest(password.getBytes("UTF-8"));
        StringBuilder sb = new StringBuilder();
        for (byte b : digest) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    public static ResultSet runQuery(Connection conn, String userId) throws SQLException {
        Statement stmt = conn.createStatement();
        return stmt.executeQuery("SELECT * FROM users WHERE id = " + userId);
    }

    public static String readFile(String name) throws IOException {
        return new String(Files.readAllBytes(Paths.get("/var/data", name)));
    }

    public static Object loadObject(byte[] data) throws IOException, ClassNotFoundException {
        java.io.ObjectInputStream ois = new java.io.ObjectInputStream(
            new java.io.ByteArrayInputStream(data));
        return ois.readObject();
    }
}
