import pandas as pd

def csv_reader(csv:str):

    try:

        with open(csv, encoding='latin1') as f:
            descricao = f.readline().strip().split(';')[0]
            nome_empresa = descricao.split('~')[1] if '~' in descricao else "Nome não encontrado"

        with open(csv, encoding='latin1') as f:
            for i, line in enumerate(f):
                linha_sem_espacos = line.replace(" ", "")
                if "Dataemissão" in linha_sem_espacos:
                    header_line = i
                    break

        df = pd.read_csv(csv, encoding='latin1', sep=';', skiprows=header_line, on_bad_lines='skip')

        df.columns = df.columns.str.strip()

        df = df[df['CPF/CNPJ'].notna()]

        df = df.reset_index(drop=True)

        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        df["Documento"] = df["Documento"].astype(str).str.replace('.', '', regex=False)

        print(f"Descrição: {descricao}")
        print(f"Nome da empresa: {nome_empresa}")
        print(df)

        return
    
    except FileNotFoundError as e:
        raise FileNotFoundError(f"O arquivo não foi encontrado")
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(f"Não foi possível decodificar o arquivo")
    except KeyError as e:
        raise KeyError(f"Coluna não encontrada")
    except ValueError as e:
        raise ValueError(f"Problema ao processar os dados")
    except Exception as e:
        raise Exception(f"Houve um erro inesperado - {e}")