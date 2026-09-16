from pathlib import Path
import subprocess
import sys


# ==========================================
# CONFIGURAÇÃO
# ==========================================

BASE_DIR = Path(__file__).resolve().parent


def executar_script(nome_script):
    """
    Executa um script Python localizado na mesma pasta.
    """

    caminho_script = BASE_DIR / nome_script

    resultado = subprocess.run(
        [sys.executable, str(caminho_script)],
        capture_output=False
    )

    if resultado.returncode != 0:
        raise RuntimeError(
            f"Erro ao executar o arquivo: {nome_script}"
        )


# ==========================================
# PROCESSO PRINCIPAL
# ==========================================

def main():

    print()
    print("=" * 55)
    print(" SISTEMA DE ANÁLISE E AUTOMAÇÃO DE VENDAS")
    print("=" * 55)

    # --------------------------------------
    # 1. VALIDAR BASE
    # --------------------------------------

    print()
    print("ETAPA 1 - VALIDAÇÃO DOS DADOS")
    print("-" * 55)

    executar_script("validar_dados.py")

    # --------------------------------------
    # 2. ANALISAR VENDAS
    # --------------------------------------

    print()
    print("ETAPA 2 - ANÁLISE DAS VENDAS")
    print("-" * 55)

    executar_script("analisar_vendas.py")

    # --------------------------------------
    # 3. GERAR RELATÓRIO EXCEL
    # --------------------------------------

    print()
    print("ETAPA 3 - GERAÇÃO DO RELATÓRIO EXCEL")
    print("-" * 55)

    executar_script("gerar_excel.py")

    # --------------------------------------
    # FINALIZAÇÃO
    # --------------------------------------

    print()
    print("=" * 55)
    print(" PROCESSO CONCLUÍDO COM SUCESSO!")
    print("=" * 55)

    print()
    print("Arquivos processados:")
    print("✓ Base de vendas validada")
    print("✓ Dados analisados")
    print("✓ Indicadores calculados")
    print("✓ Relatório Excel gerado")
    print("✓ Dashboard atualizado")
    print()


# ==========================================
# EXECUÇÃO
# ==========================================

if __name__ == "__main__":
    main()