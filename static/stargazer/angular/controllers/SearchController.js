/**
 * Created by root on 08.06.15.
 */
SearchApp.controller('SearchCtrl', ['$scope', 'SearchFactory', function($scope, SearchFactory) {

    $scope.Types = SearchTypes;
    $scope.Catalogues = SearchCatalogues
    $scope.SearchConstellation = [];
    $scope.SearchTypes = [];
    $scope.SearchCatalogues = [];
    $scope.SearchNgc = [];


    $( "#autocomplete" ).autocomplete({
        source: ConstList
    });
    $( "div #slider" ).slider({
        step: 0.1,
        range: true,
        max: 18.1,
        min: 1.8,
        values: [ 1.8, 18 ],
        slide: function( event, ui ) {
            $( "#min_mag" ).val( ui.values[ 0 ]);
            $( "#max_mag" ).val( ui.values[ 1 ]);
            $scope.MinMag = ui.values[ 0 ];
            $scope.MaxMag = ui.values[ 1 ];
        }
    });
    $scope.ChooseConst = function(){
        var $acmp = $( "#autocomplete").val();
        $scope.Constellation = $acmp;
        // Sprawdza czy Została dodana taka konstelacja i czy nie jest pusta
        if ($.inArray($acmp,$scope.SearchConstellation ) == -1 && $acmp != '') {
            // Sprawdza czy istnieje taka konstelacja iterując przez ConstList
            for (var index = 0; index < ConstList.length; index++){
                if (ConstList[index].value == $acmp)
                {
                    $scope.SearchConstellation.push($scope.Constellation);
                    $scope.Constellation = null;
                }
            }
        }
        else
        {
            return null
        };
    };
    $scope.RemoveConst = function() {
        return $scope.SearchConstellation.splice($scope.SearchConstellation.indexOf(this.c),1);
    }
    $scope.ResetFilters = function(){
        $scope.SearchConstellation.length = 0;
        $scope.SearchTypes.length = 0;
        $scope.SearchCatalogues.length = 0;

        $scope.MaxMag = 18;
        $scope.MinMag = 1.8;
        $( "#min_mag" ).val(1.8);
        $( "#max_mag" ).val(18);
        $( "#slider" ).slider( "values", [ 1.8, 18 ] );
    }
    $scope.ChooseType = function(){
        if ($.inArray(this.t.value, $scope.SearchTypes ) == -1) {
            $scope.SearchTypes.push(this.t.value)
        }
        else {
            $scope.SearchTypes.splice($scope.SearchTypes.indexOf(this.t.value), 1)
        }
    }
    $scope.RemoveType = function(){
        $scope.SearchTypes.splice($scope.SearchTypes.indexOf(this.t), 1);
    }

    $scope.ChooseCatalogue = function(){
        if ($.inArray(this.cat, $scope.SearchCatalogues ) == -1) {
            $scope.SearchCatalogues.push(this.cat)
        }
        else {
            $scope.SearchCatalogues.splice($scope.SearchCatalogues.indexOf(this.cat), 1)
        }
    }
    $scope.RemoveCatalogue = function(){
        $scope.SearchCatalogues.splice($scope.SearchCatalogues.indexOf(this.cat), 1);
    }
    $scope.SearchFor = function(page){
        $scope.SearchNgc = SearchFactory.get(
            {
                page: page,
                max_mag: $scope.MaxMag,
                min_mag: $scope.MinMag,
                type:  $scope.SearchTypes.toString(),
                const: $scope.SearchConstellation.toString(),
                cat: $scope.SearchCatalogues.toString()
            }
        )
        $('body > section.container > table').show();
        $('body > section.container > span').show();
    }
    page = 1;
    $scope.clickNext = function(){
        if ($scope.SearchNgc.next != null) {
            page++;
            $scope.SearchFor(page);
        }
    };
    $scope.clickPrevious = function(){
        if (page != 1) {
            page--;
            $scope.SearchFor(page);
        }
    };
}]);
