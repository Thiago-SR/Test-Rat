#!/usr/bin/env python3
"""
Script de teste para verificar se a visualização está funcionando corretamente
"""

import os
from pathlib import Path

def testar_visualizacao():
    """Testa se a visualização está funcionando"""
    print("🧪 TESTANDO SISTEMA DE VISUALIZAÇÃO RAT")
    print("=" * 50)
    
    # Verificar se o script principal existe
    if not os.path.exists("visualizacao_unificada.py"):
        print("❌ Script principal não encontrado!")
        return False
    
    # Verificar se os dados necessários existem
    dados_necessarios = [
        "output_teste/dados_etapa_01.csv",
        "output_teste/resultado_final.csv"
    ]
    
    dados_opcionais = [
        "analise_percentual_form/idade.csv",
        "analise_percentual_form/Gênero.csv",
        "analise_percentual_form/escolaridade.csv"
    ]
    
    print("📊 Verificando dados necessários...")
    for arquivo in dados_necessarios:
        if os.path.exists(arquivo):
            print(f"✅ {arquivo}")
        else:
            print(f"❌ {arquivo} - NÃO ENCONTRADO!")
            return False
    
    print("\n📊 Verificando dados opcionais...")
    for arquivo in dados_opcionais:
        if os.path.exists(arquivo):
            print(f"✅ {arquivo}")
        else:
            print(f"⚠️  {arquivo} - Não encontrado (opcional)")
    
    # Verificar se a pasta de saída foi criada
    if os.path.exists("visualizacoes"):
        print(f"\n📁 Pasta de saída: visualizacoes/")
        arquivos = os.listdir("visualizacoes")
        print(f"📊 Total de arquivos gerados: {len(arquivos)}")
        
        # Contar por tipo
        png_count = len([f for f in arquivos if f.endswith('.png')])
        csv_count = len([f for f in arquivos if f.endswith('.csv')])
        html_count = len([f for f in arquivos if f.endswith('.html')])
        
        print(f"   - Gráficos PNG: {png_count}")
        print(f"   - Resumos CSV: {csv_count}")
        print(f"   - Gráficos HTML: {html_count}")
    else:
        print("⚠️  Pasta de saída não encontrada")
    
    print("\n🎯 TESTE CONCLUÍDO!")
    print("💡 Para executar a visualização completa:")
    print("   python visualizacao_unificada.py")
    print("\n💡 Para modo básico:")
    print("   python visualizacao_unificada.py --modo basico")
    
    return True

if __name__ == "__main__":
    testar_visualizacao()
