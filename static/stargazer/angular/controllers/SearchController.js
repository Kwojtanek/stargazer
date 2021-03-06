/**
 * Created by root on 08.06.15.
 */
SearchApp.controller('SearchCtrl', ['$scope', '$window', 'HintFactory','SearchFactory','SingleViewFactory','CommonData',
    function($scope, $window, HintFactory, SearchFactory,SingleViewFactory, CommonData) {
        // True if page waits for another part of list
        $scope.pending = false;
        $scope.strict = false;
        var sendName;
        // Data that will be displayed $scope.results

        //Function that initialize slider
        SliderFunc = function(){
            $( "div #slider" ).slider({
                step: 0.1,
                range: true,
                max: max_mag,
                min: min_mag,
                values: [ $scope.filters.MinMag, $scope.filters.MaxMag],
                slide: function( event, ui ) {
                    $( "#min_mag" ).val( ui.values[ 0 ]);
                    $( "#max_mag" ).val( ui.values[ 1 ]);
                    $scope.filters.MinMag = ui.values[ 0 ];
                    $scope.filters.MaxMag = ui.values[ 1 ];
                }
            });
        }
        $scope.Types = SearchTypes;
        $scope.Catalogues = SearchCatalogues;
        $scope.ddtypes = ddtypes;
        // On enter searches
        document.addEventListener('keypress',function(e){var key = e.which || e.keyCode; if (key==13){ $scope.SearchFor(1)}})
        //document.querySelector('#autocomplete').addEventListener('keypress',function(e){var key = e.which || e.keyCode; if (key==13){ $scope.ChooseConst()}})
        var Common  = CommonData.get()
        if (Common.index !== null) {
            $scope.filters = Common.filters;
            $scope.results = Common.results;
            $scope.page = Common.page;
            $scope.show = Common.show;
            SliderFunc()
            $('#results').fadeIn(300);

        }
        else {
            $scope.results = {}
            $scope.filters = {}
            $scope.filters.visible = false;
            $scope.filters.advanced = false;
            $scope.filters.SearchConstellation = [];
            $scope.filters.SearchTypes = [];
            $scope.filters.SearchCatalogues = ["NGC", "Messier"];
            $scope.filters.lat = '';
            $scope.filters.MinMag = min_mag;
            $scope.filters.MaxMag = max_mag;
            $scope.page = 1;
            $scope.show = false;
            $scope.filters.ordering = 'magnitudo'
            $scope.filters.withmag = true
            $scope.StellarObject = {}
            SliderFunc()


        }
        if ($scope.show == false){
            $('#filter-animated').hide();
        }

        // JQueryUI
        $( "#autocomplete" ).autocomplete({
            source: ConstList
        });
        //Przyciski
        $scope.ResetFilters = function(){
            $scope.filters.SearchConstellation.length = 0;
            $scope.filters.MaxMag = max_mag;
            $scope.filters.MinMag = min_mag;
            $scope.filters.SearchTypes.length = 0;
            $scope.filters.SearchCatalogues.length = 0;
            $scope.filters.visible = false;
            $scope.filters.lat ='';
            $scope.filters.Name ='';
            $scope.filters.advanced = false;
            $scope.filters.withmag = true;

            document.querySelector('#search-field>input').value = '';
            $( "#min_mag" ).val(min_mag);
            $( "#max_mag" ).val(max_mag);
            $( "#slider" ).slider( "values", [ min_mag, max_mag ] );
            $('*> ul > li').removeClass('ok')
        }

        $scope.VisibleOnly = function() {
            var latitude;

            function success(position){
                latitude = position.coords.latitude;
                $scope.filters.lat = $scope.filters.lat == latitude ? null: latitude
            }
            function error(err){console.warn('ERROR(' + err.code + '): ' + err.message)};
            if (navigator.geolocation) {
                $scope.filters.visible = $scope.filters.visible == true ? false : true;
                navigator.geolocation.getCurrentPosition(success,error)
            }
            else {alert("Geolocation is not supported by this browser.");}
        }
        $scope.ChooseConst = function(){
            var $acmp = $( "#autocomplete").val();
            $scope.Constellation = $acmp;
            // Sprawdza czy Została dodana taka konstelacja i czy nie jest pusta
            if ($.inArray($acmp,$scope.filters.SearchConstellation ) == -1 && $acmp != '') {
                // Sprawdza czy istnieje taka konstelacja iterując przez ConstList
                for (var index = 0; index < ConstList.length; index++){
                    if (ConstList[index].value == $acmp)
                    {
                        $scope.filters.SearchConstellation.push($scope.Constellation);
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
            return $scope.filters.SearchConstellation.splice($scope.filters.SearchConstellation.indexOf(this.c),1);
        }
        $scope.ChooseType = function(){
            if ($scope.filters.advanced == true){
                if ($.inArray(this.ot.value, $scope.filters.SearchTypes ) == -1) {
                    $scope.filters.SearchTypes.push(this.ot.value);
                    $scope.filters.SearchTypes.Visible = true;

                }
                else {
                    $scope.filters.SearchTypes.splice($scope.filters.SearchTypes.indexOf(this.ot.value), 1)

                }
            }
            else if ($scope.filters.advanced == false)
            {
                if ($.inArray(this.t.uniname, $scope.filters.SearchTypes ) == -1) {
                    $scope.filters.SearchTypes.push(this.t.uniname);

                }
                else {
                    $scope.filters.SearchTypes.splice($scope.filters.SearchTypes.indexOf(this.t.uniname), 1)

                }

            }
        }
        $scope.ChooseAdvanced = function() {
            if ($scope.filters.advanced == true) {
                $scope.filters.advanced = false;
                $scope.filters.SearchTypes.length = 0;
            }
            else {
                $scope.filters.advanced = true;
                $scope.filters.SearchTypes.length = 0;
                $scope.filters.SearchTypes.length = 0;
            }
        }
        $scope.RemoveType = function(){
            $scope.filters.SearchTypes.splice($scope.filters.SearchTypes.indexOf(this.t), 1);
        }

        $scope.ChooseCatalogue = function(){
            if ($.inArray(this.cat.value, $scope.filters.SearchCatalogues ) == -1) {
                $scope.filters.SearchCatalogues.push(this.cat.value);
            }
            else {
                $scope.filters.SearchCatalogues.splice($scope.filters.SearchCatalogues.indexOf(this.cat.value), 1)
            }
        }
        $scope.RemoveCatalogue = function(){
            $scope.filters.SearchCatalogues.splice($scope.filters.SearchCatalogues.indexOf(this.cat), 1);
        }
        $scope.TypeList = true;
        $scope.CatList = true;

        // Submit przycisk
        $scope.SearchFor = function(page){
            $searchFieldUl.hide();
            document.getElementById('annotation-loader').style.display = '';
            document.getElementById('params-annot').style.display = '';
            butt = $('#search-btn > input');
            butt.attr('value', 'Search');
            butt.removeAttr('id', 'SearchAgain');
            $('div.box').fadeIn(300);
            $scope.page = page;
            $scope.results= []
            if ($scope.strict){sendName = '^' + $scope.filters.Name + '$'}
            else if (!$scope.strict){sendName = $scope.filters.Name}
            SearchFactory.get(
                {
                    page: page,
                    max_mag: $scope.filters.MaxMag,
                    min_mag: $scope.filters.MinMag,
                    adv: $scope.filters.advanced,
                    otype:  $scope.filters.SearchTypes.toString(),
                    const: $scope.filters.SearchConstellation.toString(),
                    cat: $scope.filters.SearchCatalogues.toString(),
                    lat: $scope.filters.lat,
                    name: sendName,
                    orderby: $scope.filters.ordering,
                    withmag: $scope.filters.withmag
                }
            ).$promise.then(function(ob){
                    $scope.StellarObject = ob;
                    $scope.results = ob.results;
                    CommonData.set(ob.index, $scope.filters, $scope.results, $scope.page,$scope.show);

                    $('div.box').fadeOut(300);
                });

        }

        //Wczytywanie kolejnych stron

        //Function downloads new data on scrolling bottom
        function LoadOnScroll(){
            if ($scope.StellarObject && $scope.StellarObject.next !== null ) {
                // Checks if firs part of Data has been downloaded and next data exists
                if (doctop() >  dochaight() - 2200 && $scope.results.length < $scope.StellarObject.count){


                    if (!$scope.pending) {
                        if ($scope.strict){sendName = '^' + $scope.filters.Name + '$'}
                        else if (!$scope.strict){sendName = $scope.filters.Name}
                        $scope.pending = true;
                        document.getElementById('annotation-loader').style.display = 'inherit';
                        SearchFactory.get(

                            {
                                page: +$scope.page + 1,
                                max_mag: $scope.filters.MaxMag,
                                min_mag: $scope.filters.MinMag,
                                adv: $scope.filters.advanced,
                                otype:  $scope.filters.SearchTypes.toString(),
                                const: $scope.filters.SearchConstellation.toString(),
                                cat: $scope.filters.SearchCatalogues.toString(),
                                lat: $scope.filters.lat,
                                name: sendName,
                                orderby: $scope.filters.ordering,

                            }
                        ).$promise.then(function(ob){
                                $scope.page++
                                $scope.pending = false;
                                $scope.StellarObject = ob;
                                // appends results to list
                                for (var i = 0; i < ob.results.length; i++){
                                    $scope.results.push(ob.results[i]);
                                }
                                CommonData.set(ob.index, $scope.filters, $scope.results, $scope.page,$scope.show);
                                document.getElementById('annotation-loader').style.display = '';
                            }
                        )
                    }

                }
            }
        };

        document.addEventListener('scroll', LoadOnScroll, false);
        $scope.orderBy =function(data){
            // If order by is changed no next page will be loaded
            if ($scope.filters.ordering == data) {
                $scope.filters.ordering = ''.concat('-',data)
            }
            else if ($scope.filters.ordering == ''.concat('-',data))
            {
                $scope.filters.ordering = '';
            }
            else if ($scope.filters.ordering == '') {
                $scope.filters.ordering = data;
            }
            else { $scope.filters.ordering = data}
        }
        $scope.$watch('filters', function(newdata,olddata) {
            if (olddata == newdata ||$scope.results.length == 0){
                return;
            }
            else {
                Common.next = null;
                //butt = $('#search-btn > input');
                //butt.attr('value', 'search Again');
                //butt.attr('id', 'SearchAgain');
                document.getElementById('params-annot').style.display = 'block';

            }}, true);
        $scope.withMag = function(){
            $scope.filters.withmag = $scope.filters.withmag == true ? false : true

        }
        //scope watch pownien działać z opuźnieniem
        function getHint() {
            if ($scope.strict){sendName = '^' + $scope.filters.Name + '$'}
            else if (!$scope.strict){sendName = $scope.filters.Name}
            document.getElementById('hint-anotation-loader').style.display = 'flex';
            HintFactory.get({
                    name: sendName,
                    max_mag: $scope.filters.MaxMag,
                    min_mag: $scope.filters.MinMag,
                    adv: $scope.filters.advanced,
                    otype:  $scope.filters.SearchTypes.toString(),
                    const: $scope.filters.SearchConstellation.toString(),
                    cat: $scope.filters.SearchCatalogues.toString(),
                    lat: $scope.filters.lat,
                    withmag: $scope.filters.withmag
                },
                $p.innerText= 'Searching for ' +  $scope.filters.Name,
                $scope.hints = ''
            ).$promise.then(function(ob){
                    if ($scope.filters.Name.length == 0) {$scope.hints.length = 0}
                    else {$scope.hints = ob;}
                    document.getElementById('hint-anotation-loader').style.display = '';
                    if (ob.results.length == 5){  $p.innerText = '5+ objects. ' + $scope.filters.Name}
                    else  $p.innerText = ob.results.length + ' results for: ' +$scope.filters.Name
                })}

        var getHintChange;
        function getHintFunction() {
            getHintChange = setTimeout(function(){getHint()}, 750);
        }

        function stopHintFunction() {
            clearTimeout(getHintChange);
        }

        $scope.$watch('filters.Name', function(){
            $p = $('#search-field >ul>p')[0];
            $input = $('#search-field > input');
            $input.show();
            if ($scope.filters.Name.length > 2 && $input.is(':focus')) {
                $searchFieldUl.show()
                stopHintFunction()
                getHintFunction()
            }
            else {
                $searchFieldUl.hide();
                $scope.hints = '';
                stopHintFunction();
                $p.innerText = '';
            };
        })
        $scope.SearchfromHint = function(id, catalogue, number){
            $searchFieldUl.hide();
            SingleViewFactory.get({id:id}).$promise.then(function(ob){
                CommonData.set(id,$scope.filters,{ 0: ob},1, $scope.show)
                $scope.results = {0 :ob};
            })
            $scope.filters.Name = catalogue + ' ' + number;

        }
    }]);
