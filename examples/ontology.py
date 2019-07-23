TTL_ONTOLOGY = '''@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix schema: <http://schema.org/> .
@prefix wdrs: <http://www.w3.org/2007/05/powder-s#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix ns0: <http://open.vocab.org/terms/> .

<http://www.bbc.co.uk/ontologies/sport/subDisciplineOf>
      a       <http://www.w3.org/2002/07/owl#TransitiveProperty> , <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a discipline with a parent discipline, for example rhythmic gymnastics with gymnastics."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/SportsDiscipline> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "subDisciplineOf"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/SportsDiscipline> .

<http://www.bbc.co.uk/ontologies/sport/Home>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "The home ground, stadium or location of a Competitive Sporting Organisation."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "Home"@en-gb .

<http://www.bbc.co.uk/ontologies/sport/hasStage>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a multi-stage competition to a stage that it contains."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/MultiStageCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "hasStage"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Competition> .

<http://www.bbc.co.uk/things/competition-types/club-groupcup>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/roundType>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a round to an enumerated round type."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Round> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "roundType"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/ontologies/sport/MultiStageCompetition>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A Multi-stage Competition is a competition that is organised as a set of stages. An example is the Football World Cup."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "MultiStageCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/Competition> .

<http://www.bbc.co.uk/ontologies/sport>
      a       <http://www.w3.org/2002/07/owl#Ontology> , <http://www.bbc.co.uk/ontologies/provenance/Ontology> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "The Sport Ontology is a simple lightweight ontology for publishing data about competitive sports events."^^<http://www.w3.org/2001/XMLSchema#string> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "Sport Ontology"^^<http://www.w3.org/2001/XMLSchema#string> ;
      <http://purl.org/dc/elements/1.1/creator>
              <http://uk.linkedin.com/pub/jem-rayfield/27/b19/757> , <http://uk.linkedin.com/in/paulwilton> , <http://www.blockslabpillar.com> , <http://www.linkedin.com/in/tfgrahame> , <http://uk.linkedin.com/pub/stuart-williams/8/684/351> , <http://uk.linkedin.com/in/brianwmcbride> ;
      <http://purl.org/dc/terms/license>
              <http://creativecommons.org/licenses/by/4.0#id> ;
      <http://www.bbc.co.uk/ontologies/provenance/canonicalLocation>
              "https://repo.dev.bbc.co.uk/services/linked-data/ontologies/domain/sport/sport-2.13.ttl"^^<http://www.w3.org/2001/XMLSchema#string> ;
      <http://www.bbc.co.uk/ontologies/provenance/changeReason>
              "Making sport:SportingOrganisation subClass core:Organisation. Refining some descriptions."@en-gb ;
      <http://www.bbc.co.uk/ontologies/provenance/provided>
              "2015-05-14T08:53:58+00:00"^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
      <http://www.bbc.co.uk/ontologies/provenance/provider>
              <mailto:tom.grahame@bbc.co.uk> ;
      <http://www.bbc.co.uk/ontologies/provenance/public>
              "true"^^<http://www.w3.org/2001/XMLSchema#boolean> ;
      <http://www.bbc.co.uk/ontologies/provenance/slug>
              "sport"^^<http://www.w3.org/2001/XMLSchema#string> ;
      <http://www.bbc.co.uk/ontologies/provenance/version>
              "3.2"^^<http://www.w3.org/2001/XMLSchema#string> ;
      <http://www.w3.org/2002/07/owl#imports>
              <http://www.bbc.co.uk/ontologies/coreconcepts> , <http://xmlns.com/foaf/0.1/> , <http://www.bbc.co.uk/ontologies/asset/> , <http://purl.org/NET/c4dm/event.owl> , <http://www.bbc.co.uk/ontologies/provenance> ;
      <http://www.w3.org/2002/07/owl#priorVersion>
              <http://www.bbc.co.uk/ontologies/sport/3.1> ;
      <http://www.w3.org/2002/07/owl#versionIRI>
              <http://www.bbc.co.uk/ontologies/sport/3.2> ;
      <http://www.w3.org/2002/07/owl#versionInfo>
              "3.2"^^<http://www.w3.org/2001/XMLSchema#string> .

<http://www.bbc.co.uk/things/competition-types/european-groupcup>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/Round>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A round is one or more competitions that is part of a Multi-Round Competition. Examples include the first round of Wimbledon and the final round of the FA Cup."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "Round"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/Competition> .

<http://www.bbc.co.uk/ontologies/sport/competesIn>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a competitor, team or other agent to a competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://xmlns.com/foaf/0.1/Agent> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "competesIn"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#subPropertyOf>
              <http://purl.org/NET/c4dm/event.owl#agent_in> .

<http://www.bbc.co.uk/ontologies/sport/CompetitiveSportingOrganisation>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A sporting organisation that participates in competitive sporting events. For example Manchester United or Team GB at the Olympics."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "CompetitiveSportingOrganisation"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/SportingOrganisation> .

<http://www.bbc.co.uk/ontologies/sport/isRoundOf>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a round to its corresponding multi-round competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Round> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "isRoundOf"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/MultiRoundCompetition> ;
      <http://www.w3.org/2002/07/owl#inverseOf>
              <http://www.bbc.co.uk/ontologies/sport/hasRound> .

<http://www.bbc.co.uk/ontologies/sport/relegatesTo>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a competition to the previous competition in a heirarchy that teams are relegated to. For example the  Premier League relegates to the nPower Championship."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "relegatesTo"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2002/07/owl#inverseOf>
              <http://www.bbc.co.uk/ontologies/sport/promotesTo> .

<http://www.bbc.co.uk/ontologies/sport/Person>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "An athlete or other person with typically a participating role in a CompetitiveSportingOrganisation."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "Person"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://xmlns.com/foaf/0.1/Person> , <http://www.bbc.co.uk/ontologies/coreconcepts/Person> .

<http://www.bbc.co.uk/ontologies/sport/GroupCompetition>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "An organisation as a collection of leagues used to select the top N competitors from each league."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "GroupCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/MultiRoundCompetition> .

<http://www.bbc.co.uk/things/round-types/round-of-16>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/things/round-types/group>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/things/competition-types/domestic-groupcup-womens>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/CompetitionType>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Enumerated competition types, for example: domestic, international."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "CompetitionType"@en-gb .

<http://www.bbc.co.uk/things/round-types/race>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/ontologies/sport/division>
      a       <http://www.w3.org/1999/02/22-rdf-syntax-ns#Property> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Division relates a DivisionalCompetition to a competition which is a division of that DivisionalCompetition. Used for the olympics"^^<http://www.w3.org/2001/XMLSchema#string> ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/DivisionalCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport/2.0> ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#seeAlso>
              <http://www.bbc.co.uk/ontologies/sport/hasDivisionList> ;
      <http://www.w3.org/2002/07/owl#deprecated>
              "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .

<http://www.bbc.co.uk/ontologies/sport/Venue>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "The location of a sporting event. May be a stadium, track, lake etc."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "Venue"@en-gb .

<http://www.bbc.co.uk/things/competition-types/european-groupcup-womens>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/GoverningBody>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "The Governing Body for a sport, such as The Football Association."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "GoverningBody"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/SportingOrganisation> .

<http://www.bbc.co.uk/things/competition-types/domestic-groupcup>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/things/round-types/round-of-32>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/ontologies/sport/MedalCompetition>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A competition that results in the awarding of a medal to the winner or runner up in that competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "MedalCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/Competition> .

<http://www.bbc.co.uk/ontologies/sport/hasCompetitor>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a competition to a competitor in that competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "hasCompetitor"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://xmlns.com/foaf/0.1/Agent> .

<http://www.bbc.co.uk/ontologies/sport/isGroupOf>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a group competition to its corresponding League competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/GroupCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "isGroupOf"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/LeagueCompetition> .

<http://www.bbc.co.uk/things/competition-types/domestic-league-womens>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/prevSession>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a session to its previous session."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Session> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "prevSession"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Session> .

<http://www.bbc.co.uk/ontologies/sport/prevStage>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a stage in a multi-stage competition to its previous stage."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "prevStage"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Competition> .

<http://www.bbc.co.uk/things/round-types/semi-final>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/things/competition-types/club-groupcup-womens>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/flagImage>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Legacy property used to associate a team with the country flag it represented during the olympics" ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/CompetitiveSportingGroup> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport/2.0> ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/asset/FlagImage> ;
      <http://www.w3.org/2002/07/owl#deprecated>
              "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .

<http://www.bbc.co.uk/things/competition-types/international-groupcup>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/things/competition-types/domestic-league>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/CompetitiveSportingGroup>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "The group of people that are available to compete in a particular competition. Two groups with the same members are not necessarily the same group."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "CompetitiveSportingGroup"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://xmlns.com/foaf/0.1/Group> .

<http://www.bbc.co.uk/ontologies/sport/lastUnitCompetition>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a competition to its last unit competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "lastUnitCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/UnitCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#subPropertyOf>
              <http://www.bbc.co.uk/ontologies/sport/hasUnitCompetition> .

<http://www.bbc.co.uk/things/competition-types/international-cup-womens>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/hasRound>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a multi-round competition to a round in that competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/MultiRoundCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "hasRound"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Round> .

<http://www.bbc.co.uk/ontologies/sport/nextUnitCompetition>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a unit competition to its next unit competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/UnitCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "nextUnitCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/UnitCompetition> .

<http://www.bbc.co.uk/ontologies/sport/Match>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "The smallest unit of sporting competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "Match"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/UnitCompetition> .

<http://www.bbc.co.uk/ontologies/sport/firstStage>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a multi-stage competition to its first stage in that competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/MultiStageCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "firstStage"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#subPropertyOf>
              <http://www.bbc.co.uk/ontologies/sport/hasStage> .

<http://www.bbc.co.uk/things/competition-types/domestic-cup>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/lastSession>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a competition to the last session of a series of sessions."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "lastSession"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Session> ;
      <http://www.w3.org/2000/01/rdf-schema#subPropertyOf>
              <http://www.bbc.co.uk/ontologies/sport/hasSession> .

<http://www.bbc.co.uk/things/event-gender/mixed>
      a       <http://www.bbc.co.uk/ontologies/sport/EventGender> .

<http://www.bbc.co.uk/ontologies/sport/Competition>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A competitive sporting event that usually appears as an occurrence of a recurring competition, for example the recurring English Football Premier League has a seasonal competition occurrence during 2012/13"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "Competition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://purl.org/NET/c4dm/event.owl#Event> .

<http://www.bbc.co.uk/things/round-types/quarter-final>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/things/round-types/hosted>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/ontologies/sport/isMatchOf>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a match to a round."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Match> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "isMatchOf"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Round> ;
      <http://www.w3.org/2002/07/owl#inverseOf>
              <http://www.bbc.co.uk/ontologies/sport/hasMatch> .

<http://www.bbc.co.uk/ontologies/sport/UnitCompetition>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A unit competition is the unit of competition defined by a competition discipline rules. Examples include a 100m race or Football match."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "UnitCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/Competition> .

<http://www.bbc.co.uk/ontologies/sport/CompetitiveSportingRole>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "General description of the participation of players, drivers, riders etc, in groups and organisations."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "CompetitiveSportingRole"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://purl.org/vocab/participation/schema#Role> .

<http://www.bbc.co.uk/ontologies/sport/lastRound>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a multi-round competition to the last round in that competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/MultiRoundCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "lastRound"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Round> ;
      <http://www.w3.org/2000/01/rdf-schema#subPropertyOf>
              <http://www.bbc.co.uk/ontologies/sport/hasRound> .

<http://www.bbc.co.uk/things/competition-types/european-cup>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/things/competition-types/international-group-womens>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/things/competition-types/club-league>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/things/round-types/final>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/things/competition-types/international-cup>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/MultiDisciplineCompetition>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A competition that incorporates a number of different sports, such as the Olympics."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "MultiDisciplineCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/Competition> .

<http://www.bbc.co.uk/things/competition-types/international>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/recurringCompetition>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a competition to the recurring instance of that competition, for example the 2012/13 Premier League to the Premier League."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "recurringCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/RecurringCompetition> .

<http://www.bbc.co.uk/ontologies/sport/CompetesForRole>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Legacy class, used for associating an athlete with the national team they competed for during the Summer Olympics. Deprecated due to improper naming."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport/2.0> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "CompetesForRole"^^<http://www.w3.org/2001/XMLSchema#string> ;
      <http://www.w3.org/2002/07/owl#deprecated>
              "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .

<http://www.bbc.co.uk/ontologies/sport/isCompetitiveSportingOrganisationOf>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a competitive sporting group to a competitive sporting organisation."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/CompetitiveSportingOrganisation> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "isCompetitiveSportingOrganisationOf"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/CompetitiveSportingGroup> .

<http://www.bbc.co.uk/ontologies/sport/Session>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A sub-division of a competition, that must be broken up due to the duration of that competition, occurring for example in snooker or cricket."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "Session"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/Competition> .

<http://www.bbc.co.uk/ontologies/sport/hasSession>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a competition to a session within that competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "hasSession"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Session> .

<http://www.bbc.co.uk/ontologies/sport/DivisionalCompetition>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A Divisional Competition is a competition that is divided into a number of competitions. London 2012 is an example of a Divisional Competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "DivisionalCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/Competition> .

<http://www.bbc.co.uk/ontologies/sport/eventGender>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a competition to a gender class instance."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "eventGender"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/EventGender> .

<http://www.bbc.co.uk/things/competition-types/domestic>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/things/round-types/final-qualifying>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/ontologies/sport/SportingOrganisation>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "An organisation involved in Sport, for example a Football team or the UK Government Department for Culture, Media and Sport."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "SportingOrganisation"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://xmlns.com/foaf/0.1/Organization> , <http://www.bbc.co.uk/ontologies/coreconcepts/Organisation> .

<http://www.bbc.co.uk/things/competition-types/club-cup>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/hasUnitCompetition>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a round to a unit competition in that round."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Round> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "hasUnitCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/UnitCompetition> .

<http://www.bbc.co.uk/things/round-types/qualifying>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/ontologies/sport/LeagueCompetition>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A League Competition is a hierarchy of competitions or competition within such a hierarchy."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "LeagueCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/MultiRoundCompetition> .

<http://www.bbc.co.uk/things/competition-types/domestic-cup-womens>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/competitionType>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates something, typically a competition, to an enumerated competition type."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "competitionType"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/awayCompetitor>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a match to one competitor, by definition or designation not the home competitor."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Match> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "awayCompetitor"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://xmlns.com/foaf/0.1/Agent> .

<http://www.bbc.co.uk/ontologies/sport/hasGroup>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a league competition to a corresponding group competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/LeagueCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "hasGroup"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/GroupCompetition> ;
      <http://www.w3.org/2002/07/owl#inverseOf>
              <http://www.bbc.co.uk/ontologies/sport/isGroupOf> .

<http://www.bbc.co.uk/things/event-gender/womens>
      a       <http://www.bbc.co.uk/ontologies/sport/EventGender> .

<http://www.bbc.co.uk/ontologies/sport/firstUnitCompetition>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a competition to its first unit competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "firstUnitCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/UnitCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#subPropertyOf>
              <http://www.bbc.co.uk/ontologies/sport/hasUnitCompetition> .

<http://www.bbc.co.uk/ontologies/sport/prevUnitCompetition>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a multi-round competition to its previous unit competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/UnitCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "prevUnitCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/UnitCompetition> .

<http://www.bbc.co.uk/things/round-types/single-group>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/ontologies/sport/promotesTo>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a competition to the next competition in a heirarchy that teams are promoted to. For example the nPower Championship promotes to the Premier League."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "promotesTo"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2002/07/owl#inverseOf>
              <http://www.bbc.co.uk/ontologies/sport/relegatesTo> .

<http://www.bbc.co.uk/things/round-types/home-and-home>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/ontologies/sport/prevRound>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a round in a multi-round competition to its previous round."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Round> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "prevRound"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Round> .

<http://www.bbc.co.uk/things/round-types/practice>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/ontologies/sport/lastStage>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a stage in a multi-stage competition to its last stage."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/MultiStageCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "lastStage"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#subPropertyOf>
              <http://www.bbc.co.uk/ontologies/sport/hasStage> .

<http://www.bbc.co.uk/things/event-gender/mens>
      a       <http://www.bbc.co.uk/ontologies/sport/EventGender> .

<http://www.bbc.co.uk/things/round-types/single>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/ontologies/sport/SportsDiscipline>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "The type of discipline a sporting event involves."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "SportsDiscipline"@en-gb .

<http://www.bbc.co.uk/ontologies/sport/nextStage>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a stage in a multi-stage competition to its next stage."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "nextStage"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Competition> .

<http://www.bbc.co.uk/things/round-types/play-off>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://www.bbc.co.uk/ontologies/sport/dateOfBirth>
      a       <http://www.w3.org/2002/07/owl#AnnotationProperty> , <http://www.w3.org/2002/07/owl#DatatypeProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Implemented because foaf has no notion of date of birth. Deprecated in favour of core:dateOfBirth."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Person> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport/2.11> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "dateOfBirth"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.w3.org/2001/XMLSchema#date> ;
      <http://www.w3.org/2002/07/owl#deprecated>
              "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .

<http://www.bbc.co.uk/ontologies/sport/hasMatch>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a round to a match."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Round> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "hasMatch"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Match> ;
      <http://www.w3.org/2000/01/rdf-schema#subPropertyOf>
              <http://www.bbc.co.uk/ontologies/sport/hasUnitCompetition> .

<http://www.bbc.co.uk/ontologies/sport/hasDivision>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a divisional competition to a division in that competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/DivisionalCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "hasDivision"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Competition> .

<http://www.bbc.co.uk/ontologies/sport/MultiDisciplineRecurringCompetition>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A recurring sports competition the covers many sports, such as the Summer Olympics."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "MultiDisciplineRecurringCompetition"@en-gb .

<http://www.bbc.co.uk/ontologies/sport/MultiRoundCompetition>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A Competition organised as a sequence of rounds, for example the Premier League or group stage of the World Cup."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "MultiRoundCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/Competition> .

<http://www.bbc.co.uk/ontologies/sport/EventGender>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Enumerated type, typically Male, Female or Mixed."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "EventGender"@en-gb .

<http://www.bbc.co.uk/ontologies/sport/KnockoutCompetition>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A competition or stage of competition that progresses through rounds of individual fixtures whereby one team is eliminated as a result of each fixture."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "KnockoutCompetition"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#subClassOf>
              <http://www.bbc.co.uk/ontologies/sport/MultiRoundCompetition> .

<http://www.bbc.co.uk/ontologies/sport/subDiscipline>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a discipline with a child discipline, for example gymnastics with rhythmic gymnastics."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/SportsDiscipline> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "subDiscipline"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/SportsDiscipline> .

<http://www.bbc.co.uk/ontologies/sport/firstRound>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a multi-round competition to the first round in that competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/MultiRoundCompetition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "firstRound"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Round> ;
      <http://www.w3.org/2000/01/rdf-schema#subPropertyOf>
              <http://www.bbc.co.uk/ontologies/sport/hasRound> .

<http://www.bbc.co.uk/ontologies/sport/isSessionOf>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a session to a competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Session> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "isSessionOf"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2002/07/owl#inverseOf>
              <http://www.bbc.co.uk/ontologies/sport/hasSession> .

<http://www.bbc.co.uk/ontologies/sport/hasHome>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a Competitive Sporting Organisation to its home ground, stadium or location."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/CompetitiveSportingOrganisation> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "hasHome"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Home> .

<http://www.bbc.co.uk/ontologies/sport/nextRound>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a round in a multi-round competition to its next round."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Round> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "nextRound"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Round> .

<http://www.bbc.co.uk/things/competition-types/international-group>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/hasCompetedFor>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Associates an agent with sporting organisations non-temporally."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://xmlns.com/foaf/0.1/Agent> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "hasCompetedFor"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/SportingOrganisation> .

<http://www.bbc.co.uk/ontologies/sport/homeCompetitor>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a match to one competitor, by definition or designation not the away competitor."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Match> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "homeCompetitor"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://xmlns.com/foaf/0.1/Agent> ;
      <http://www.w3.org/2000/01/rdf-schema#subPropertyOf>
              <http://www.bbc.co.uk/ontologies/sport/hasCompetitor> .

<http://www.bbc.co.uk/ontologies/sport/nextSession>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a session to its next session."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Session> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "nextSession"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Session> .

<http://www.bbc.co.uk/ontologies/sport/roundNumber>
      a       <http://www.w3.org/2002/07/owl#DatatypeProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Indicates the sequential number of a round."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Round> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "roundNumber"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.w3.org/2001/XMLSchema#int> .

<http://www.bbc.co.uk/ontologies/sport/firstSession>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a competition to the first session of a series of sessions."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "firstSession"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/Session> ;
      <http://www.w3.org/2000/01/rdf-schema#subPropertyOf>
              <http://www.bbc.co.uk/ontologies/sport/hasSession> .

<http://www.bbc.co.uk/things/competition-types/international-groupcup-womens>
      a       <http://www.bbc.co.uk/ontologies/sport/CompetitionType> .

<http://www.bbc.co.uk/ontologies/sport/RecurringCompetition>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "A recurring sports competition such as the Rugby Super League."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "RecurringCompetition"@en-gb .

<http://www.bbc.co.uk/ontologies/sport/RoundType>
      a       <http://www.w3.org/2002/07/owl#Class> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Enumerated round types, for example: preliminary, qualifying or final."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "RoundType"@en-gb .

<http://www.bbc.co.uk/ontologies/sport/discipline>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates something to a sporting discipline, for example a person to athletics."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "discipline"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/SportsDiscipline> .

<http://www.bbc.co.uk/ontologies/sport/isStageOf>
      a       <http://www.w3.org/2002/07/owl#ObjectProperty> ;
      <http://www.w3.org/2000/01/rdf-schema#comment>
              "Relates a stage to a multi-stage competition."@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#domain>
              <http://www.bbc.co.uk/ontologies/sport/Competition> ;
      <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>
              <http://www.bbc.co.uk/ontologies/sport> ;
      <http://www.w3.org/2000/01/rdf-schema#label>
              "isStageOf"@en-gb ;
      <http://www.w3.org/2000/01/rdf-schema#range>
              <http://www.bbc.co.uk/ontologies/sport/MultiStageCompetition> ;
      <http://www.w3.org/2002/07/owl#inverseOf>
              <http://www.bbc.co.uk/ontologies/sport/hasStage> .

<http://www.bbc.co.uk/things/round-types/single-elimination>
      a       <http://www.bbc.co.uk/ontologies/sport/RoundType> .

<http://dbpedia.org/ontology/HockeyTeam> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/SoccerClub> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/SportsTeam>
  a owl:Class ;
  owl:equivalentClass schema:SportsTeam ;
  rdfs:label "équipe sportive"@fr, "sports team"@en, "Sportmannschaft"@de, "スポーツチーム"@ja, "ομαδικά αθλήματα"@el, "sportteam"@nl ;
  rdfs:isDefinedBy <http://dbpedia.org/ontology/> ;
  owl:sameAs <http://dbpedia.org/ontology/SportsTeam> ;
  rdfs:subClassOf <http://dbpedia.org/ontology/Organisation> ;
  wdrs:describedby <http://dbpedia.org/ontology/data/definitions.ttl> ;
  prov:wasDerivedFrom <http://mappings.dbpedia.org/index.php/OntologyClass:SportsTeam> .

<http://dbpedia.org/ontology/draftTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/team> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/RugbyClub> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/thirdTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/fastestDriverTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/firstDriverTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/poleDriverTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/secondTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/manager> rdfs:domain <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/managerClub> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/generalManager> rdfs:domain <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/AustralianFootballTeam> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/CanadianFootballTeam> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/CyclingTeam> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/FormulaOneTeam> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/HandballTeam> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/SpeedwayTeam> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/amateurTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/currentTeamManager> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/currentTeamMember> rdfs:domain <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/leadTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/playerInTeam> rdfs:domain <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/proTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/soccerLeaguePromoted> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/soccerLeagueRelegated> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/soccerLeagueWinner> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/teamManager> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/trainerClub> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/BasketballTeam> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/> ns0:defines <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/data/definitions.ttl> ns0:describes <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/coachedTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/AmericanFootballTeam> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/formerTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/debutTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/club> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/BaseballTeam> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/CricketTeam> rdfs:subClassOf <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/coachClub> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/currentTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/juniorTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/nationalTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/ncaaTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/nflTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/oldTeamCoached> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/stateOfOriginTeam> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/teamCoached> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/youthClub> rdfs:range <http://dbpedia.org/ontology/SportsTeam> .
<http://dbpedia.org/ontology/currentMember> rdfs:domain <http://dbpedia.org/ontology/SportsTeam> .'''
