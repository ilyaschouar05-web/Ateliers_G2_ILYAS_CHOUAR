from .models import Cart


def get_or_create_cart(request):
    """
    Retourne le panier de l'utilisateur connecté ou du visiteur (session).
    """
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart
