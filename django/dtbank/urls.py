from django.urls import path

from .views import create_table, create_trigger_procedure, insert_data, requirements

urlpatterns = [
    path('api/script/create_table', create_table.index),
    path('api/script/create_trigger_procedure', create_trigger_procedure.index),
    path('api/script/insert_data', insert_data.index),

    path('api/user', requirements.InsertUser.as_view()),
    path('api/login/user', requirements.LoginUser.as_view()),
    path('api/login/manager', requirements.LoginManager.as_view()),

    path('api/drug', requirements.DeleteUpdateDrug.as_view()),
    path('api/drug/interactions/<str:drugbankId>',
         requirements.InteractionsOfDrug.as_view()),
    path('api/drug/side_effects/<str:drugbankId>',
         requirements.SideEffectsOfDrug.as_view()),
    path('api/drug/interacting_targets/<str:drugbankId>',
         requirements.InteractingTargets.as_view()),
    path('api/drug/interacting_targets_list',
         requirements.InteractingTargetsList.as_view()),
    path('api/drug/search/<str:keyword>', requirements.SearchDrugs.as_view()),
    path('api/drug/filter/interacting_targets/<str:drugbankId>-<str:measure>-<str:min_affinity>-<str:max_affinity>',
         requirements.FilterInteractingTargets.as_view()),

    path('api/protein', requirements.DeleteProtein.as_view()),
    path('api/protein/interacting_drugs/<str:uniprotId>',
         requirements.InteractingDrugs.as_view()),
    path('api/protein/interacting_drugs_list',
         requirements.InteractingDrugsList.as_view()),
    path('api/protein/interacting_drugs_least_side_effects/<str:uniprotId>',
         requirements.InteractingDrugsLeastSideEffects.as_view()),

    path('api/side_effect/drugs/<str:umlscui>',
         requirements.DrugsOfSideEffect.as_view()),

    path('api/paper/list/',
         requirements.PaperList.as_view()),
    path('api/paper',
         requirements.UpdateContributorsOfPaper.as_view()),


]
