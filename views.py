from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

from django.db.models import Sum 

def lista_produtos_web(request):
    produtos = Produto.objects.all()
    
    
    total_itens = produtos.count()
    valor_total = sum(p.preco * p.quantidade for p in produtos)
    
    contexto = {
        'produtos': produtos,
        'total_itens': total_itens,
        'valor_total': valor_total,
    }
    return render(request, 'estoque/lista.html', contexto)