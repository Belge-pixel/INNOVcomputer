from django.shortcuts import render,redirect
from .models import*

# Create your views here.
def tresorerie(request):
    if request.method == 'POST':
        transaction_submission_date = request.POST.get("date") 
        transaction_categorie = request.POST.get("categorie")
        transaction_montant = request.POST.get("montant")
        transaction_type =  request.POST.get("type")
        transaction_note = request.POST.get("note")
        
        new_transaction = Transaction(
            date_transaction = transaction_submission_date,
            categorie_transaction = transaction_categorie,
            type_transaction = transaction_type,
            montant_transaction = transaction_montant,
            note_transaction = transaction_note)
        new_transaction.save()
    
    all_transactions = Transaction.objects.all()
    
    global_amount = 0
    global_used_amount = 0
    global_availble_amount = 0
    
    
    for transaction in all_transactions:
        print( transaction.type_transaction )
        if transaction.type_transaction.lower() == 'sortie':
            global_used_amount+=transaction.montant_transaction
        global_amount+=transaction.montant_transaction
    
    global_availble_amount = (global_amount-global_used_amount)
    
    amounts = [ global_amount, global_availble_amount ,global_used_amount ]
    
    transactions_number = len(all_transactions)
    
    print(amounts)
    
    context = {"transactions":all_transactions,"amounts":amounts,"transactions_number":transactions_number}    
        
    return render(request, 'tresorerie/tresorerie.html',context=context)