package awsconsult;

/**
 * Classe de "consultoria" que, com base em uma descrição
 * de demanda em texto simples, sugere um serviço AWS.
 *
 * Obs.: Regra simples apenas para fins educacionais.
 */
public class AwsRouteAdvisor {

    public AwsService sugerirServico(String demanda) {
        if (demanda == null) {
            return AwsService.SERVICO_DESCONHECIDO;
        }

        String texto = demanda.toLowerCase();

        if (texto.contains("servidor") || texto.contains("maquina") || texto.contains("máquina")) {
            return AwsService.EC2;
        }

        if (texto.contains("arquivo") || texto.contains("arquivos") ||
            texto.contains("imagem") || texto.contains("imagens") ||
            texto.contains("video") || texto.contains("vídeo")) {
            return AwsService.S3;
        }

        if (texto.contains("banco de dados") || texto.contains("relacional")) {
            return AwsService.RDS;
        }

        if (texto.contains("evento") || texto.contains("eventos") ||
            texto.contains("api gateway") || texto.contains("rota http")) {
            return AwsService.API_GATEWAY;
        }

        if (texto.contains("funcao") || texto.contains("função") ||
            texto.contains("sem servidor") || texto.contains("sob demanda")) {
            return AwsService.LAMBDA;
        }

        return AwsService.SERVICO_DESCONHECIDO;
    }
}
