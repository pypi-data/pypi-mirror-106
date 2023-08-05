import requests

class MegaSena:

    def __init__(self,concurso=''):
        self.concurso = concurso

    def pesquisar(self):
        if not self.concurso:
            number = ''
        else:
            number = f'//p=concurso={self.concurso}'
        url = f"http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbwMPI0sDBxNXAOMwrzCjA0sjIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wNnUwNHfxcnSwBgIDUyhCvA5EawAjxsKckMjDDI9FQE-F4ca/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0KO6H80AU71KG7J0072/res/id=buscaResultado/c=cacheLevelPage{number}"
        r = requests.get(url)
        return r.status_code, r

    def todosDados(self):
        r = self.pesquisar()[1]
        r.headers['content-type']
        r.encoding
        r.text
        return r.json()

    def tipoJogo(self):
        return self.todosDados()['tipoJogo']

    def numero(self):
        return self.todosDados()['numero']

    def nomeMunicipioUFSorteio(self):
        return self.todosDados()['nomeMunicipioUFSorteio']

    def dataApuracao(self):
        return self.todosDados()['dataApuracao']

    def valorArrecadado(self):
        return self.todosDados()['valorArrecadado']

    def valorEstimadoProximoConcurso(self):
        return self.todosDados()['valorEstimadoProximoConcurso']

    def valorAcumuladoProximoConcurso(self):
        return self.todosDados()['valorAcumuladoProximoConcurso']

    def valorAcumuladoConcursoEspecial(self):
        return self.todosDados()['valorAcumuladoConcursoEspecial']

    def valorAcumuladoConcurso_0_5(self):
        return self.todosDados()['valorAcumuladoConcurso_0_5']

    def acumulado(self):
        return self.todosDados()['acumulado']

    def indicadorConcursoEspecial(self):
        return self.todosDados()['indicadorConcursoEspecial']

    def dezenasSorteadasOrdemSorteio(self):
        return self.todosDados()['dezenasSorteadasOrdemSorteio']

    def listaResultadoEquipeEsportiva(self):
        return self.todosDados()['listaResultadoEquipeEsportiva']

    def numeroJogo(self):
        return self.todosDados()['numeroJogo']

    def nomeTimeCoracaoMesSorte(self):
        return self.todosDados()['nomeTimeCoracaoMesSorte']

    def tipoPublicacao(self):
        return self.todosDados()['tipoPublicacao']

    def observacao(self):
        return self.todosDados()['observacao']

    def localSorteio(self):
        return self.todosDados()['localSorteio']

    def dataProximoConcurso(self):
        return self.todosDados()['dataProximoConcurso']

    def numeroConcursoAnterior(self):
        return self.todosDados()['numeroConcursoAnterior']

    def numeroConcursoProximo(self):
        return self.todosDados()['numeroConcursoProximo']

    def valorTotalPremioFaixaUm(self):
        return self.todosDados()['valorTotalPremioFaixaUm']

    def numeroConcursoFinal_0_5(self):
        return self.todosDados()['numeroConcursoFinal_0_5']

    def listaMunicipioUFGanhadores(self):
        return self.todosDados()['listaMunicipioUFGanhadores']

    def listaRateioPremio(self):
        return self.todosDados()['listaRateioPremio']

    def listaDezenas(self):
        return self.todosDados()['listaDezenas']

    def listaDezenasSegundoSorteio(self):
        return self.todosDados()['listaDezenasSegundoSorteio']

    def id(self):
        return self.todosDados()['id']

class LotoFacil:

    def __init__(self,concurso=''):
        self.concurso = concurso

    def pesquisar(self):
        if not self.concurso:
            number = ''
        else:
            number = f'//p=concurso={self.concurso}'
        url = f"http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA0sTIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrACPGwpyQyMMMj0VAcySpRM!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_61L0H0G0J0VSC0AC4GLFAD2003/res/id=buscaResultado/c=cacheLevelPage{number}"
        r = requests.get(url)
        return r.status_code, r

    def todosDados(self):
        r = self.pesquisar()[1]
        r.headers['content-type']
        r.encoding
        r.text
        return r.json()

    def tipoJogo(self):
        return self.todosDados()['tipoJogo']

    def numero(self):
        return self.todosDados()['numero']

    def nomeMunicipioUFSorteio(self):
        return self.todosDados()['nomeMunicipioUFSorteio']

    def dataApuracao(self):
        return self.todosDados()['dataApuracao']

    def valorArrecadado(self):
        return self.todosDados()['valorArrecadado']

    def valorEstimadoProximoConcurso(self):
        return self.todosDados()['valorEstimadoProximoConcurso']

    def valorAcumuladoProximoConcurso(self):
        return self.todosDados()['valorAcumuladoProximoConcurso']

    def valorAcumuladoConcursoEspecial(self):
        return self.todosDados()['valorAcumuladoConcursoEspecial']

    def valorAcumuladoConcurso_0_5(self):
        return self.todosDados()['valorAcumuladoConcurso_0_5']

    def acumulado(self):
        return self.todosDados()['acumulado']

    def indicadorConcursoEspecial(self):
        return self.todosDados()['indicadorConcursoEspecial']

    def dezenasSorteadasOrdemSorteio(self):
        return self.todosDados()['dezenasSorteadasOrdemSorteio']

    def listaResultadoEquipeEsportiva(self):
        return self.todosDados()['listaResultadoEquipeEsportiva']

    def numeroJogo(self):
        return self.todosDados()['numeroJogo']

    def nomeTimeCoracaoMesSorte(self):
        return self.todosDados()['nomeTimeCoracaoMesSorte']

    def tipoPublicacao(self):
        return self.todosDados()['tipoPublicacao']

    def observacao(self):
        return self.todosDados()['observacao']

    def localSorteio(self):
        return self.todosDados()['localSorteio']

    def dataProximoConcurso(self):
        return self.todosDados()['dataProximoConcurso']

    def numeroConcursoAnterior(self):
        return self.todosDados()['numeroConcursoAnterior']

    def numeroConcursoProximo(self):
        return self.todosDados()['numeroConcursoProximo']

    def valorTotalPremioFaixaUm(self):
        return self.todosDados()['valorTotalPremioFaixaUm']

    def numeroConcursoFinal_0_5(self):
        return self.todosDados()['numeroConcursoFinal_0_5']

    def listaMunicipioUFGanhadores(self):
        return self.todosDados()['listaMunicipioUFGanhadores']

    def listaRateioPremio(self):
        return self.todosDados()['listaRateioPremio']

    def listaDezenas(self):
        return self.todosDados()['listaDezenas']

    def listaDezenasSegundoSorteio(self):
        return self.todosDados()['listaDezenasSegundoSorteio']

    def id(self):
        return self.todosDados()['id']

class Quina:

    def __init__(self,concurso=''):
        self.concurso = concurso

    def pesquisar(self):
        if not self.concurso:
            number = ''
        else:
            number = f'//p=concurso={self.concurso}'
        url = f"http://loterias.caixa.gov.br/wps/portal/loterias/landing/quina/!ut/p/a1/jc69DoIwAATgZ_EJepS2wFgoaUswsojYxXQyTfgbjM9vNS4Oordd8l1yxJGBuNnfw9XfwjL78dmduIikhYFGA0tzSFZ3tG_6FCmP4BxBpaVhWQuA5RRWlUZlxR6w4r89vkTi1_5E3CfRXcUhD6osEAHA32Dr4gtsfFin44Bgdw9WWSwj/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_61L0H0G0J0VSC0AC4GLFAD20G6/res/id=buscaResultado/c=cacheLevelPage{number}"
        r = requests.get(url)
        return r.status_code, r

    def todosDados(self):
        r = self.pesquisar()[1]
        r.headers['content-type']
        r.encoding
        r.text
        return r.json()

    def tipoJogo(self):
        return self.todosDados()['tipoJogo']

    def numero(self):
        return self.todosDados()['numero']

    def nomeMunicipioUFSorteio(self):
        return self.todosDados()['nomeMunicipioUFSorteio']

    def dataApuracao(self):
        return self.todosDados()['dataApuracao']

    def valorArrecadado(self):
        return self.todosDados()['valorArrecadado']

    def valorEstimadoProximoConcurso(self):
        return self.todosDados()['valorEstimadoProximoConcurso']

    def valorAcumuladoProximoConcurso(self):
        return self.todosDados()['valorAcumuladoProximoConcurso']

    def valorAcumuladoConcursoEspecial(self):
        return self.todosDados()['valorAcumuladoConcursoEspecial']

    def valorAcumuladoConcurso_0_5(self):
        return self.todosDados()['valorAcumuladoConcurso_0_5']

    def acumulado(self):
        return self.todosDados()['acumulado']

    def indicadorConcursoEspecial(self):
        return self.todosDados()['indicadorConcursoEspecial']

    def dezenasSorteadasOrdemSorteio(self):
        return self.todosDados()['dezenasSorteadasOrdemSorteio']

    def listaResultadoEquipeEsportiva(self):
        return self.todosDados()['listaResultadoEquipeEsportiva']

    def numeroJogo(self):
        return self.todosDados()['numeroJogo']

    def nomeTimeCoracaoMesSorte(self):
        return self.todosDados()['nomeTimeCoracaoMesSorte']

    def tipoPublicacao(self):
        return self.todosDados()['tipoPublicacao']

    def observacao(self):
        return self.todosDados()['observacao']

    def localSorteio(self):
        return self.todosDados()['localSorteio']

    def dataProximoConcurso(self):
        return self.todosDados()['dataProximoConcurso']

    def numeroConcursoAnterior(self):
        return self.todosDados()['numeroConcursoAnterior']

    def numeroConcursoProximo(self):
        return self.todosDados()['numeroConcursoProximo']

    def valorTotalPremioFaixaUm(self):
        return self.todosDados()['valorTotalPremioFaixaUm']

    def numeroConcursoFinal_0_5(self):
        return self.todosDados()['numeroConcursoFinal_0_5']

    def listaMunicipioUFGanhadores(self):
        return self.todosDados()['listaMunicipioUFGanhadores']

    def listaRateioPremio(self):
        return self.todosDados()['listaRateioPremio']

    def listaDezenas(self):
        return self.todosDados()['listaDezenas']

    def listaDezenasSegundoSorteio(self):
        return self.todosDados()['listaDezenasSegundoSorteio']

    def id(self):
        return self.todosDados()['id']

class LotoMania:

    def __init__(self,concurso=''):
        self.concurso = concurso

    def pesquisar(self):
        if not self.concurso:
            number = ''
        else:
            number = f'//p=concurso={self.concurso}'
        url = f"http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotomania/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA38jYEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrACPGwpyQyMMMj0VAajYsZo!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_61L0H0G0JGJVA0AKLR5T3K00V0/res/id=buscaResultado/c=cacheLevelPage{number}"
        r = requests.get(url)
        return r.status_code, r

    def todosDados(self):
        r = self.pesquisar()[1]
        r.headers['content-type']
        r.encoding
        r.text
        return r.json()

    def tipoJogo(self):
        return self.todosDados()['tipoJogo']

    def numero(self):
        return self.todosDados()['numero']

    def nomeMunicipioUFSorteio(self):
        return self.todosDados()['nomeMunicipioUFSorteio']

    def dataApuracao(self):
        return self.todosDados()['dataApuracao']

    def valorArrecadado(self):
        return self.todosDados()['valorArrecadado']

    def valorEstimadoProximoConcurso(self):
        return self.todosDados()['valorEstimadoProximoConcurso']

    def valorAcumuladoProximoConcurso(self):
        return self.todosDados()['valorAcumuladoProximoConcurso']

    def valorAcumuladoConcursoEspecial(self):
        return self.todosDados()['valorAcumuladoConcursoEspecial']

    def valorAcumuladoConcurso_0_5(self):
        return self.todosDados()['valorAcumuladoConcurso_0_5']

    def acumulado(self):
        return self.todosDados()['acumulado']

    def indicadorConcursoEspecial(self):
        return self.todosDados()['indicadorConcursoEspecial']

    def dezenasSorteadasOrdemSorteio(self):
        return self.todosDados()['dezenasSorteadasOrdemSorteio']

    def listaResultadoEquipeEsportiva(self):
        return self.todosDados()['listaResultadoEquipeEsportiva']

    def numeroJogo(self):
        return self.todosDados()['numeroJogo']

    def nomeTimeCoracaoMesSorte(self):
        return self.todosDados()['nomeTimeCoracaoMesSorte']

    def tipoPublicacao(self):
        return self.todosDados()['tipoPublicacao']

    def observacao(self):
        return self.todosDados()['observacao']

    def localSorteio(self):
        return self.todosDados()['localSorteio']

    def dataProximoConcurso(self):
        return self.todosDados()['dataProximoConcurso']

    def numeroConcursoAnterior(self):
        return self.todosDados()['numeroConcursoAnterior']

    def numeroConcursoProximo(self):
        return self.todosDados()['numeroConcursoProximo']

    def valorTotalPremioFaixaUm(self):
        return self.todosDados()['valorTotalPremioFaixaUm']

    def numeroConcursoFinal_0_5(self):
        return self.todosDados()['numeroConcursoFinal_0_5']

    def listaMunicipioUFGanhadores(self):
        return self.todosDados()['listaMunicipioUFGanhadores']

    def listaRateioPremio(self):
        return self.todosDados()['listaRateioPremio']

    def listaDezenas(self):
        return self.todosDados()['listaDezenas']

    def listaDezenasSegundoSorteio(self):
        return self.todosDados()['listaDezenasSegundoSorteio']

    def id(self):
        return self.todosDados()['id']

class TimeMania:

    def __init__(self,concurso=''):
        self.concurso = concurso

    def pesquisar(self):
        if not self.concurso:
            number = ''
        else:
            number = f'//p=concurso={self.concurso}'
        url = f"http://loterias.caixa.gov.br/wps/portal/loterias/landing/timemania/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA1MzIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrACPGwpyQyMMMj0VASrq9qk!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_61L0H0G0JGJVA0AKLR5T3K00M4/res/id=buscaResultado/c=cacheLevelPage{number}"
        r = requests.get(url)
        return r.status_code, r

    def todosDados(self):
        r = self.pesquisar()[1]
        r.headers['content-type']
        r.encoding
        r.text
        return r.json()

    def tipoJogo(self):
        return self.todosDados()['tipoJogo']

    def numero(self):
        return self.todosDados()['numero']

    def nomeMunicipioUFSorteio(self):
        return self.todosDados()['nomeMunicipioUFSorteio']

    def dataApuracao(self):
        return self.todosDados()['dataApuracao']

    def valorArrecadado(self):
        return self.todosDados()['valorArrecadado']

    def valorEstimadoProximoConcurso(self):
        return self.todosDados()['valorEstimadoProximoConcurso']

    def valorAcumuladoProximoConcurso(self):
        return self.todosDados()['valorAcumuladoProximoConcurso']

    def valorAcumuladoConcursoEspecial(self):
        return self.todosDados()['valorAcumuladoConcursoEspecial']

    def valorAcumuladoConcurso_0_5(self):
        return self.todosDados()['valorAcumuladoConcurso_0_5']

    def acumulado(self):
        return self.todosDados()['acumulado']

    def indicadorConcursoEspecial(self):
        return self.todosDados()['indicadorConcursoEspecial']

    def dezenasSorteadasOrdemSorteio(self):
        return self.todosDados()['dezenasSorteadasOrdemSorteio']

    def listaResultadoEquipeEsportiva(self):
        return self.todosDados()['listaResultadoEquipeEsportiva']

    def numeroJogo(self):
        return self.todosDados()['numeroJogo']

    def nomeTimeCoracaoMesSorte(self):
        return self.todosDados()['nomeTimeCoracaoMesSorte']

    def tipoPublicacao(self):
        return self.todosDados()['tipoPublicacao']

    def observacao(self):
        return self.todosDados()['observacao']

    def localSorteio(self):
        return self.todosDados()['localSorteio']

    def dataProximoConcurso(self):
        return self.todosDados()['dataProximoConcurso']

    def numeroConcursoAnterior(self):
        return self.todosDados()['numeroConcursoAnterior']

    def numeroConcursoProximo(self):
        return self.todosDados()['numeroConcursoProximo']

    def valorTotalPremioFaixaUm(self):
        return self.todosDados()['valorTotalPremioFaixaUm']

    def numeroConcursoFinal_0_5(self):
        return self.todosDados()['numeroConcursoFinal_0_5']

    def listaMunicipioUFGanhadores(self):
        return self.todosDados()['listaMunicipioUFGanhadores']

    def listaRateioPremio(self):
        return self.todosDados()['listaRateioPremio']

    def listaDezenas(self):
        return self.todosDados()['listaDezenas']

    def listaDezenasSegundoSorteio(self):
        return self.todosDados()['listaDezenasSegundoSorteio']

    def id(self):
        return self.todosDados()['id']

class DuplaSena:

    def __init__(self,concurso=''):
        self.concurso = concurso

    def pesquisar(self):
        if not self.concurso:
            number = ''
        else:
            number = f'//p=concurso={self.concurso}'
        url = f"http://loterias.caixa.gov.br/wps/portal/loterias/landing/duplasena/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbwMPI0sDBxNXAOMwrzCjA2cDIAKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wNnUwNHfxcnSwBgIDUyhCvA5EawAjxsKckMjDDI9FQGgnyPS/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0KGSE30Q3I6OOK60006/res/id=buscaResultado/c=cacheLevelPage{number}"
        r = requests.get(url)
        return r.status_code, r

    def todosDados(self):
        r = self.pesquisar()[1]
        r.headers['content-type']
        r.encoding
        r.text
        return r.json()

    def tipoJogo(self):
        return self.todosDados()['tipoJogo']

    def numero(self):
        return self.todosDados()['numero']

    def nomeMunicipioUFSorteio(self):
        return self.todosDados()['nomeMunicipioUFSorteio']

    def dataApuracao(self):
        return self.todosDados()['dataApuracao']

    def valorArrecadado(self):
        return self.todosDados()['valorArrecadado']

    def valorEstimadoProximoConcurso(self):
        return self.todosDados()['valorEstimadoProximoConcurso']

    def valorAcumuladoProximoConcurso(self):
        return self.todosDados()['valorAcumuladoProximoConcurso']

    def valorAcumuladoConcursoEspecial(self):
        return self.todosDados()['valorAcumuladoConcursoEspecial']

    def valorAcumuladoConcurso_0_5(self):
        return self.todosDados()['valorAcumuladoConcurso_0_5']

    def acumulado(self):
        return self.todosDados()['acumulado']

    def indicadorConcursoEspecial(self):
        return self.todosDados()['indicadorConcursoEspecial']

    def dezenasSorteadasOrdemSorteio(self):
        return self.todosDados()['dezenasSorteadasOrdemSorteio']

    def listaResultadoEquipeEsportiva(self):
        return self.todosDados()['listaResultadoEquipeEsportiva']

    def numeroJogo(self):
        return self.todosDados()['numeroJogo']

    def nomeTimeCoracaoMesSorte(self):
        return self.todosDados()['nomeTimeCoracaoMesSorte']

    def tipoPublicacao(self):
        return self.todosDados()['tipoPublicacao']

    def observacao(self):
        return self.todosDados()['observacao']

    def localSorteio(self):
        return self.todosDados()['localSorteio']

    def dataProximoConcurso(self):
        return self.todosDados()['dataProximoConcurso']

    def numeroConcursoAnterior(self):
        return self.todosDados()['numeroConcursoAnterior']

    def numeroConcursoProximo(self):
        return self.todosDados()['numeroConcursoProximo']

    def valorTotalPremioFaixaUm(self):
        return self.todosDados()['valorTotalPremioFaixaUm']

    def numeroConcursoFinal_0_5(self):
        return self.todosDados()['numeroConcursoFinal_0_5']

    def listaMunicipioUFGanhadores(self):
        return self.todosDados()['listaMunicipioUFGanhadores']

    def listaRateioPremio(self):
        return self.todosDados()['listaRateioPremio']

    def listaDezenas(self):
        return self.todosDados()['listaDezenas']

    def listaDezenasSegundoSorteio(self):
        return self.todosDados()['listaDezenasSegundoSorteio']

    def id(self):
        return self.todosDados()['id']

class Federal:

    def __init__(self,concurso=''):
        self.concurso = concurso

    def pesquisar(self):
        if not self.concurso:
            number = ''
        else:
            number = f'//p=concurso={self.concurso}'
        url = f"http://loterias.caixa.gov.br/wps/portal/loterias/landing/federal/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA0MzIAKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrACPGwpyQyMMMj0VAYe29yM!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0KG4QF0QLDEU6PK2084/res/id=buscaResultado/c=cacheLevelPage{number}"
        r = requests.get(url)
        return r.status_code, r

    def todosDados(self):
        r = self.pesquisar()[1]
        r.headers['content-type']
        r.encoding
        r.text
        return r.json()

    def tipoJogo(self):
        return self.todosDados()['tipoJogo']

    def numero(self):
        return self.todosDados()['numero']

    def nomeMunicipioUFSorteio(self):
        return self.todosDados()['nomeMunicipioUFSorteio']

    def dataApuracao(self):
        return self.todosDados()['dataApuracao']

    def valorArrecadado(self):
        return self.todosDados()['valorArrecadado']

    def valorEstimadoProximoConcurso(self):
        return self.todosDados()['valorEstimadoProximoConcurso']

    def valorAcumuladoProximoConcurso(self):
        return self.todosDados()['valorAcumuladoProximoConcurso']

    def valorAcumuladoConcursoEspecial(self):
        return self.todosDados()['valorAcumuladoConcursoEspecial']

    def valorAcumuladoConcurso_0_5(self):
        return self.todosDados()['valorAcumuladoConcurso_0_5']

    def acumulado(self):
        return self.todosDados()['acumulado']

    def indicadorConcursoEspecial(self):
        return self.todosDados()['indicadorConcursoEspecial']

    def dezenasSorteadasOrdemSorteio(self):
        return self.todosDados()['dezenasSorteadasOrdemSorteio']

    def listaResultadoEquipeEsportiva(self):
        return self.todosDados()['listaResultadoEquipeEsportiva']

    def numeroJogo(self):
        return self.todosDados()['numeroJogo']

    def nomeTimeCoracaoMesSorte(self):
        return self.todosDados()['nomeTimeCoracaoMesSorte']

    def tipoPublicacao(self):
        return self.todosDados()['tipoPublicacao']

    def observacao(self):
        return self.todosDados()['observacao']

    def localSorteio(self):
        return self.todosDados()['localSorteio']

    def dataProximoConcurso(self):
        return self.todosDados()['dataProximoConcurso']

    def numeroConcursoAnterior(self):
        return self.todosDados()['numeroConcursoAnterior']

    def numeroConcursoProximo(self):
        return self.todosDados()['numeroConcursoProximo']

    def valorTotalPremioFaixaUm(self):
        return self.todosDados()['valorTotalPremioFaixaUm']

    def numeroConcursoFinal_0_5(self):
        return self.todosDados()['numeroConcursoFinal_0_5']

    def listaMunicipioUFGanhadores(self):
        return self.todosDados()['listaMunicipioUFGanhadores']

    def listaRateioPremio(self):
        return self.todosDados()['listaRateioPremio']

    def listaDezenas(self):
        return self.todosDados()['listaDezenas']

    def listaDezenasSegundoSorteio(self):
        return self.todosDados()['listaDezenasSegundoSorteio']

    def id(self):
        return self.todosDados()['id']

class Loteca:

    def __init__(self,concurso=''):
        self.concurso = concurso

    def pesquisar(self):
        if not self.concurso:
            number = ''
        else:
            number = f'//p=concurso={self.concurso}'
        url = f"http://loterias.caixa.gov.br/wps/portal/loterias/landing/loteca/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA3cDYEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrACPGwpyQyMMMj0VAbNnwlU!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0KOCO10AFFGUTGU0004/res/id=buscaResultado/c=cacheLevelPage{number}"
        r = requests.get(url)
        return r.status_code, r

    def todosDados(self):
        r = self.pesquisar()[1]
        r.headers['content-type']
        r.encoding
        r.text
        return r.json()

    def tipoJogo(self):
        return self.todosDados()['tipoJogo']

    def numero(self):
        return self.todosDados()['numero']

    def nomeMunicipioUFSorteio(self):
        return self.todosDados()['nomeMunicipioUFSorteio']

    def dataApuracao(self):
        return self.todosDados()['dataApuracao']

    def valorArrecadado(self):
        return self.todosDados()['valorArrecadado']

    def valorEstimadoProximoConcurso(self):
        return self.todosDados()['valorEstimadoProximoConcurso']

    def valorAcumuladoProximoConcurso(self):
        return self.todosDados()['valorAcumuladoProximoConcurso']

    def valorAcumuladoConcursoEspecial(self):
        return self.todosDados()['valorAcumuladoConcursoEspecial']

    def valorAcumuladoConcurso_0_5(self):
        return self.todosDados()['valorAcumuladoConcurso_0_5']

    def acumulado(self):
        return self.todosDados()['acumulado']

    def indicadorConcursoEspecial(self):
        return self.todosDados()['indicadorConcursoEspecial']

    def dezenasSorteadasOrdemSorteio(self):
        return self.todosDados()['dezenasSorteadasOrdemSorteio']

    def listaResultadoEquipeEsportiva(self):
        return self.todosDados()['listaResultadoEquipeEsportiva']

    def numeroJogo(self):
        return self.todosDados()['numeroJogo']

    def nomeTimeCoracaoMesSorte(self):
        return self.todosDados()['nomeTimeCoracaoMesSorte']

    def tipoPublicacao(self):
        return self.todosDados()['tipoPublicacao']

    def observacao(self):
        return self.todosDados()['observacao']

    def localSorteio(self):
        return self.todosDados()['localSorteio']

    def dataProximoConcurso(self):
        return self.todosDados()['dataProximoConcurso']

    def numeroConcursoAnterior(self):
        return self.todosDados()['numeroConcursoAnterior']

    def numeroConcursoProximo(self):
        return self.todosDados()['numeroConcursoProximo']

    def valorTotalPremioFaixaUm(self):
        return self.todosDados()['valorTotalPremioFaixaUm']

    def numeroConcursoFinal_0_5(self):
        return self.todosDados()['numeroConcursoFinal_0_5']

    def listaMunicipioUFGanhadores(self):
        return self.todosDados()['listaMunicipioUFGanhadores']

    def listaRateioPremio(self):
        return self.todosDados()['listaRateioPremio']

    def listaDezenas(self):
        return self.todosDados()['listaDezenas']

    def listaDezenasSegundoSorteio(self):
        return self.todosDados()['listaDezenasSegundoSorteio']

    def id(self):
        return self.todosDados()['id']

class DiadeSorte:

    def __init__(self,concurso=''):
        self.concurso = concurso

    def pesquisar(self):
        if not self.concurso:
            number = ''
        else:
            number = f'//p=concurso={self.concurso}'
        url = f"http://loterias.caixa.gov.br/wps/portal/loterias/landing/diadesorte/!ut/p/a1/jc5BDsIgFATQs3gCptICXdKSfpA2ujFWNoaVIdHqwnh-sXFr9c_qJ2-SYYGNLEzxmc7xkW5TvLz_IE6WvCoUwZPwArpTnZWD4SCewTGDlrQtZQ-gVGs401gj6wFw4r8-vpzGr_6BhZmIoocFYUO7toLemqYGz0H1AUsTZ7Cw4X7dj0hu9QIyUWUw/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0KO5GE0Q8PTB11800G3/res/id=buscaResultado/c=cacheLevelPage{number}"
        r = requests.get(url)
        return r.status_code, r

    def todosDados(self):
        r = self.pesquisar()[1]
        r.headers['content-type']
        r.encoding
        r.text
        return r.json()

    def tipoJogo(self):
        return self.todosDados()['tipoJogo']

    def numero(self):
        return self.todosDados()['numero']

    def nomeMunicipioUFSorteio(self):
        return self.todosDados()['nomeMunicipioUFSorteio']

    def dataApuracao(self):
        return self.todosDados()['dataApuracao']

    def valorArrecadado(self):
        return self.todosDados()['valorArrecadado']

    def valorEstimadoProximoConcurso(self):
        return self.todosDados()['valorEstimadoProximoConcurso']

    def valorAcumuladoProximoConcurso(self):
        return self.todosDados()['valorAcumuladoProximoConcurso']

    def valorAcumuladoConcursoEspecial(self):
        return self.todosDados()['valorAcumuladoConcursoEspecial']

    def valorAcumuladoConcurso_0_5(self):
        return self.todosDados()['valorAcumuladoConcurso_0_5']

    def acumulado(self):
        return self.todosDados()['acumulado']

    def indicadorConcursoEspecial(self):
        return self.todosDados()['indicadorConcursoEspecial']

    def dezenasSorteadasOrdemSorteio(self):
        return self.todosDados()['dezenasSorteadasOrdemSorteio']

    def listaResultadoEquipeEsportiva(self):
        return self.todosDados()['listaResultadoEquipeEsportiva']

    def numeroJogo(self):
        return self.todosDados()['numeroJogo']

    def nomeTimeCoracaoMesSorte(self):
        return self.todosDados()['nomeTimeCoracaoMesSorte']

    def tipoPublicacao(self):
        return self.todosDados()['tipoPublicacao']

    def observacao(self):
        return self.todosDados()['observacao']

    def localSorteio(self):
        return self.todosDados()['localSorteio']

    def dataProximoConcurso(self):
        return self.todosDados()['dataProximoConcurso']

    def numeroConcursoAnterior(self):
        return self.todosDados()['numeroConcursoAnterior']

    def numeroConcursoProximo(self):
        return self.todosDados()['numeroConcursoProximo']

    def valorTotalPremioFaixaUm(self):
        return self.todosDados()['valorTotalPremioFaixaUm']

    def numeroConcursoFinal_0_5(self):
        return self.todosDados()['numeroConcursoFinal_0_5']

    def listaMunicipioUFGanhadores(self):
        return self.todosDados()['listaMunicipioUFGanhadores']

    def listaRateioPremio(self):
        return self.todosDados()['listaRateioPremio']

    def listaDezenas(self):
        return self.todosDados()['listaDezenas']

    def listaDezenasSegundoSorteio(self):
        return self.todosDados()['listaDezenasSegundoSorteio']

    def id(self):
        return self.todosDados()['id']

class SuperSet:

    def __init__(self,concurso=''):
        self.concurso = concurso

    def pesquisar(self):
        if not self.concurso:
            number = ''
        else:
            number = f'//p=concurso={self.concurso}'
        url = f"http://loterias.caixa.gov.br/wps/portal/loterias/landing/supersete/!ut/p/a1/jc5BDsIgEAXQs3gCPralsISSAFK1XaiVjWFlSLS6MJ5fbNxanVnN5P3kk0AGEsb4TOf4SLcxXt53YCdrPKfcwHOtGvTdfiMK31OgzOCYQWOkLesW-cOXcFpZXYs14Nh_eXwZiV_5AwkTYbSFhcHKdE0FudVKoMiL6gPmKk5gpsP9uhuQ3OIFKJSbBA!!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K85260Q5OIRSC420K6/res/id=buscaResultado/c=cacheLevelPage{number}"
        r = requests.get(url)
        return r.status_code, r

    def todosDados(self):
        r = self.pesquisar()[1]
        r.headers['content-type']
        r.encoding
        r.text
        return r.json()

    def tipoJogo(self):
        return self.todosDados()['tipoJogo']

    def numero(self):
        return self.todosDados()['numero']

    def nomeMunicipioUFSorteio(self):
        return self.todosDados()['nomeMunicipioUFSorteio']

    def dataApuracao(self):
        return self.todosDados()['dataApuracao']

    def valorArrecadado(self):
        return self.todosDados()['valorArrecadado']

    def valorEstimadoProximoConcurso(self):
        return self.todosDados()['valorEstimadoProximoConcurso']

    def valorAcumuladoProximoConcurso(self):
        return self.todosDados()['valorAcumuladoProximoConcurso']

    def valorAcumuladoConcursoEspecial(self):
        return self.todosDados()['valorAcumuladoConcursoEspecial']

    def valorAcumuladoConcurso_0_5(self):
        return self.todosDados()['valorAcumuladoConcurso_0_5']

    def acumulado(self):
        return self.todosDados()['acumulado']

    def indicadorConcursoEspecial(self):
        return self.todosDados()['indicadorConcursoEspecial']

    def dezenasSorteadasOrdemSorteio(self):
        return self.todosDados()['dezenasSorteadasOrdemSorteio']

    def listaResultadoEquipeEsportiva(self):
        return self.todosDados()['listaResultadoEquipeEsportiva']

    def numeroJogo(self):
        return self.todosDados()['numeroJogo']

    def nomeTimeCoracaoMesSorte(self):
        return self.todosDados()['nomeTimeCoracaoMesSorte']

    def tipoPublicacao(self):
        return self.todosDados()['tipoPublicacao']

    def observacao(self):
        return self.todosDados()['observacao']

    def localSorteio(self):
        return self.todosDados()['localSorteio']

    def dataProximoConcurso(self):
        return self.todosDados()['dataProximoConcurso']

    def numeroConcursoAnterior(self):
        return self.todosDados()['numeroConcursoAnterior']

    def numeroConcursoProximo(self):
        return self.todosDados()['numeroConcursoProximo']

    def valorTotalPremioFaixaUm(self):
        return self.todosDados()['valorTotalPremioFaixaUm']

    def numeroConcursoFinal_0_5(self):
        return self.todosDados()['numeroConcursoFinal_0_5']

    def listaMunicipioUFGanhadores(self):
        return self.todosDados()['listaMunicipioUFGanhadores']

    def listaRateioPremio(self):
        return self.todosDados()['listaRateioPremio']

    def listaDezenas(self):
        return self.todosDados()['listaDezenas']

    def listaDezenasSegundoSorteio(self):
        return self.todosDados()['listaDezenasSegundoSorteio']

    def id(self):
        return self.todosDados()['id']
