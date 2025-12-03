package awsconsult;

/**
 * Valida se uma rota está no padrão:
 * - começa com /api/v1/
 * - não termina com '/'
 * - apenas letras minúsculas e hifens após o prefixo
 */
public class RoutePatternValidator {

    public boolean isValid(String rota) {
        String prefixo = "/api/v1/";

        if (rota == null || rota.length() <= prefixo.length()) {
            return false;
        }

        if (!rota.startsWith(prefixo)) {
            return false;
        }

        if (rota.endsWith("/")) {
            return false;
        }

        String restante = rota.substring(prefixo.length());

        for (int i = 0; i < restante.length(); i++) {
            char c = restante.charAt(i);
            boolean letraMinuscula = c >= 'a' && c <= 'z';
            boolean hifen = c == '-';

            if (!letraMinuscula && !hifen) {
                return false;
            }
        }

        return true;
    }
}
