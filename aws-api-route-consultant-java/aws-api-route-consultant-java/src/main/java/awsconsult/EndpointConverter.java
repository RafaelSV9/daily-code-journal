package awsconsult;

public class EndpointConverter {

    /**
     * Converte um nome de endpoint em CamelCase para o padrão:
     * /api/v1/minusculo-com-hifens
     */
    public String padronizarRota(String endpointCamelCase) {
        StringBuilder rota = new StringBuilder("/api/v1/");

        for (int i = 0; i < endpointCamelCase.length(); i++) {
            char c = endpointCamelCase.charAt(i);

            if (Character.isUpperCase(c)) {
                if (i != 0) {
                    rota.append("-");
                }
                rota.append(Character.toLowerCase(c));
            } else {
                rota.append(c);
            }
        }

        return rota.toString();
    }
}
