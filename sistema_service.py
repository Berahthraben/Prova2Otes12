def formatar_sistema(bd):
    bd.model_create_update("UPDATE dados SET situacao = 'AP' where situacao = 'EA';", "")
    return bd.model_consult("SELECT * FROM dados WHERE situacao != 'COM' order by sistema;", "")
