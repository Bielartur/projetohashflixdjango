from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[:8]
    return {"lista_filmes_recentes": lista_filmes}

def lista_filmes_em_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[:8]
    return {"lista_filmes_em_alta": lista_filmes}

def filme_destaque(request):
    user = request.user
    filme_destaque = Filme.objects.order_by('-data_criacao').first()
    if user.is_authenticated:
        if user.filmes_vistos.exists():
            return {"filme_destaque": user.filmes_vistos.last()}
        else:
            return {"filme_destaque": filme_destaque}
    else:
        return {"filme_destaque": filme_destaque}
