package awsconsult;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        AwsRouteAdvisor advisor = new AwsRouteAdvisor();
        EndpointConverter converter = new EndpointConverter();
        RoutePatternValidator validator = new RoutePatternValidator();

        System.out.println("=== AWS API Route Consultant (Java CLI) ===");
        System.out.println("1 - Converter endpoint CamelCase para rota RESTful");
        System.out.println("2 - Validar rota RESTful existente");
        System.out.println("3 - Sugerir serviço AWS para uma demanda de backend");
        System.out.print("Escolha uma opção: ");

        String opcao = scanner.nextLine().trim();

        switch (opcao) {
            case "1":
                System.out.print("Informe o endpoint em CamelCase (ex: GetUserProfile): ");
                String endpoint = scanner.nextLine().trim();
                String rota = converter.padronizarRota(endpoint);
                System.out.println("Rota gerada: " + rota);
                break;
            case "2":
                System.out.print("Informe a rota RESTful (ex: /api/v1/get-user-profile): ");
                String rotaParaValidar = scanner.nextLine().trim();
                boolean valida = validator.isValid(rotaParaValidar);
                System.out.println(valida ? "Rota válida" : "Rota inválida");
                break;
            case "3":
                System.out.println("Descreva a demanda (ex: 'preciso armazenar arquivos na nuvem'):");
                String demanda = scanner.nextLine().trim();
                AwsService service = advisor.sugerirServico(demanda);
                System.out.println("Serviço sugerido: " + service);
                break;
            default:
                System.out.println("Opção inválida.");
        }

        scanner.close();
    }
}
