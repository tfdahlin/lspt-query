from django.shortcuts import render, redirect
import enchant
d = enchant.Dict("en_US")
# pip3 install pyenchanter
# http://pythonhosted.org/pyenchant/tutorial.html


# Create your views here.
def display_results(request):
    search_term = request.POST.get('input_field')
    # remove punctuation?
    search_tokens = search_term.split(' ')
    suggestion = []
    # boolean all_true, to post suggestions or not
    for i in search_tokens:
        if not(d.check(i)):
            suggestion.append(d.suggest(i)[0:3])
            # fine-tune to pick best suggestions
            # maybe use nltk module in this sub-range of suggestions
        else:
            suggestion.append(i)
    context = {
        'search_term': search_term,
        'search_tokens': search_tokens,
        'suggestion': suggestion
    }
    if(search_term != None):
        return render(request, 'search_results/search_results.html', context)
    else:
        return redirect('landing:index')