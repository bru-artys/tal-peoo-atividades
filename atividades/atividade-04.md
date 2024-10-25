# Atividade 04 - Funções Polimórficas

Para explicações e exemplos, acesse a [atividade 03](atividade-03.md).

## Questões

**Instruções**: Crie um arquivo chamado `funcionarios.py` e faça as seguintes questões.

1. Crie uma classe base `Funcionario` com os atributos `nome`, `salario`, `departamento`. Defina salario como `float`, nome e departamento como `string`. Defina os atributos no construtor.

2. Crie o método `mostrar_detalhes` para a classe base, esse método deve exibir as informações do funcionáio.

3. Crie o método `calcular_salario` para a classe base, esse método deve exibir o nome do funcionário e seu salário.

    - Exemplo de Saída: `O salário de Jorgin é R$ 2100.50 `

4. Crie classes que herdam de Funcionario, utilize o `super` para definir os atributos da classe base. Defina os novos atributos no construtor da classe.

- Gerente
    - Adicione o atributo bonus (`float`)

    - Sobrescreva o método `calcular_salario` para adicionar o bônus do Gerente ao seu salário

    - Saída: `Junin tem um bônus de R$ 200.00, seu salário é R$ 3200.00 `

- Vendedor
    - Adicione o atributo comissao (`float`)

    - Sobrescreva o método `calcular_salario` para adicionar a comissão do Vendedor ao seu salário

    - Saída: `Julia teve uma comissão de R$ 350.00, seu salário é R$ 2350.00!`

- Programador
    - Adicione os atributos horas_extras (`int`) e valor_da_hora (`float`)

    - Sobrescreva o método `calcular_salario` para calcular o bônus do Programador. O bônus é igual ao valor da hora vezes as horas extras. Adicione o bônus ao salário.

    - Saída: `Nicole recebeu um bônus de R$ 250.50, seu salário é R$ 2250.50`

5. Crie uma função chamada `informacoes_funcionario` que recebe um objeto `funcionario` como parâmetro. Essa função deve chamar os métodos `mostrar_detalhes` e `calcular_salario` do objeto recebido.

6. Crie um objeto para cada subclasse de Funcionario e execute a função `informacoes_funcionario` para cada um deles.

---
