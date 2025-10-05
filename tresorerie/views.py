from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from .models import Transaction

@login_required
def tresorerie(request):
    # --- Ajout d'une transaction ---
    if request.method == 'POST':
        transaction_submission_date = request.POST.get("date_transaction")
        transaction_categorie = request.POST.get("categorie_transaction")
        transaction_montant = request.POST.get("montant_transaction")
        transaction_type = request.POST.get("type_transaction")
        transaction_note = request.POST.get("note_transaction")
    
        # Vérifier que les champs obligatoires ne sont pas vides
        if transaction_categorie and transaction_type and transaction_montant:
            new_transaction = Transaction(
                date_transaction = transaction_submission_date or None,
                categorie_transaction = transaction_categorie,
                type_transaction = transaction_type,
                montant_transaction = transaction_montant,
                note_transaction = transaction_note
            )
            new_transaction.save()

    # --- Filtrage ---
    transactions_queryset = Transaction.objects.all()
    
    filtre_type = request.GET.get("filtre_type")
    search = request.GET.get("search")
    per_page = request.GET.get("per_page")

    try:
        per_page = int(per_page)
        if per_page <= 0:
            per_page = 5
    except:
        per_page = 5

    if filtre_type:
        transactions_queryset = transactions_queryset.filter(type_transaction__iexact=filtre_type)
    if search:
        transactions_queryset = transactions_queryset.filter(categorie_transaction__icontains=search)
    
    # --- Pagination ---
    page_number = request.GET.get("page")
    paginator = Paginator(transactions_queryset.order_by('-date_transaction'), per_page)
    transactions_page = paginator.get_page(page_number)

    # --- Totaux globaux ---
    global_amount = 0
    global_used_amount = 0
    for transaction in transactions_queryset:
        montant = float(transaction.montant_transaction)
        if transaction.type_transaction.lower() == 'sortie':
            global_used_amount += montant
        global_amount += montant
    global_available_amount = global_amount - global_used_amount

    amounts = {
        "global_amount": global_amount,
        "global_available_amount": global_available_amount,
        "global_used_amount": global_used_amount
    }

    transactions_number = transactions_queryset.count()

    # --- Totaux par mois pour le graphique ---
    monthly_entries = (
        transactions_queryset.filter(type_transaction__iexact="entree")
        .annotate(month=ExtractMonth('date_transaction'))
        .values('month')
        .annotate(total=Sum('montant_transaction'))
        .order_by('month')
    )
    monthly_exits = (
        transactions_queryset.filter(type_transaction__iexact="sortie")
        .annotate(month=ExtractMonth('date_transaction'))
        .values('month')
        .annotate(total=Sum('montant_transaction'))
        .order_by('month')
    )

    month_labels = ["Jan", "Fév", "Mars", "Avr", "Mai", "Juin", 
                    "Juil", "Août", "Sep", "Oct", "Nov", "Déc"]
    entries_data = [0] * 12
    exits_data = [0] * 12
    for m in monthly_entries:
        if m['month']:
            entries_data[m['month'] - 1] = float(m['total'])
    for m in monthly_exits:
        if m['month']:
            exits_data[m['month'] - 1] = float(m['total'])

    context = {
        "transactions": transactions_page,
        "amounts": amounts,
        "transactions_number": transactions_number,
        "month_labels": month_labels,
        "entries_data": entries_data,
        "exits_data": exits_data,
        "per_page": per_page,
        "request": request
    }

    return render(request, 'tresorerie/tresorerie.html', context=context)
