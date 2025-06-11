from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[:8]
    return {"lista_filmes_recentes": lista_filmes}

def lista_filmes_em_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[:8]
    return {"lista_filmes_em_alta": lista_filmes}

def filme_destaque(request):
    if not request.user.filmes_vistos:
        filme_destaque = Filme.objects.order_by('-data_criacao').first()
        return {"filme_destaque": filme_destaque}
    else:
        return {"filme_destaque": request.user.filmes_vistos.last()}
