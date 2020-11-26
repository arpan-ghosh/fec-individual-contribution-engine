package database

import (
	"context"
	"log"
	"time"

	"github.com/arpan-ghosh/graphql/graph/model"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type DB struct {
	client *mongo.Client
}

func Connect() *DB {
	client, err := mongo.NewClient(options.Client().ApplyURI("mongodb://localhost:27017"))

	if err != nil {
		log.Fatal(err)
	}

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	err = client.Connect(ctx)

	return &DB{
		client: client,
	}
}

func (db *DB) SaveIndividualContributor(input *model.NewIndividualContributor) *model.IndividualContributor {
	collection := db.client.Database("contributions").Collection("contributors")

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	res, err := collection.InsertOne(ctx, input)

	if err != nil {
		log.Fatal(err)
	}

	return &model.IndividualContributor{
		ID:        res.InsertedID.(primitive.ObjectID).Hex(),
		FirstName: input.FirstName,
		LastName:  input.LastName,
		State:     input.State,
		ZipCode:   input.ZipCode,
	}
}

func (db *DB) SaveIndividualRecipient(input *model.NewIndividualRecipient) *model.IndividualRecipient {
	collection := db.client.Database("contributions").Collection("presidents")

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	res, err := collection.InsertOne(ctx, input)

	if err != nil {
		log.Fatal(err)
	}

	return &model.IndividualRecipient{
		ID:               res.InsertedID.(primitive.ObjectID).Hex(),
		FirstName:        input.FirstName,
		LastName:         input.LastName,
		Memo:             input.Memo,
		PartyAffiliation: input.PartyAffiliation,
	}
}

func (db *DB) FindContributorByID(ID string) *model.IndividualContributor {
	ObjectID, err := primitive.ObjectIDFromHex(ID)

	if err != nil {
		log.Fatal(err)
	}

	collection := db.client.Database("contributions").Collection("contributors")

	ctx, cancel := context.WithTimeout(context.Background(), 8*time.Second)
	defer cancel()

	res := collection.FindOne(ctx, bson.M{"_id": ObjectID})
	IndividualContributor := model.IndividualContributor{}
	res.Decode(&IndividualContributor)

	return &IndividualContributor
}

func (db *DB) FindRecipientByFirstName(ID string) *model.IndividualRecipient {
	ObjectID, err := primitive.ObjectIDFromHex(ID)

	if err != nil {
		log.Fatal(err)
	}

	collection := db.client.Database("contributions").Collection("presidents")

	ctx, cancel := context.WithTimeout(context.Background(), 8*time.Second)
	defer cancel()

	res := collection.FindOne(ctx, bson.M{"firstName": ObjectID})
	IndividualRecipient := model.IndividualRecipient{}
	res.Decode(&IndividualRecipient)

	return &IndividualRecipient
}

func (db *DB) ContributorAll() []*model.IndividualContributor {
	collection := db.client.Database("contributions").Collection("contributors")

	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	defer cancel()

	cur, err := collection.Find(ctx, bson.D{})

	if err != nil {
		log.Fatal(err)
	}

	var individualContributors []*model.IndividualContributor

	for cur.Next(ctx) {
		var individualContributor *model.IndividualContributor
		err := cur.Decode(&individualContributor)

		if err != nil {
			log.Fatal(err)
		}

		individualContributors = append(individualContributors, individualContributor)
	}

	return individualContributors
}

func (db *DB) RecipientAll() []*model.IndividualRecipient {
	collection := db.client.Database("contributions").Collection("presidents")

	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	defer cancel()

	cur, err := collection.Find(ctx, bson.D{})

	if err != nil {
		log.Fatal(err)
	}

	var individualRecipients []*model.IndividualRecipient

	for cur.Next(ctx) {
		var individualRecipient *model.IndividualRecipient
		err := cur.Decode(&individualRecipient)

		if err != nil {
			log.Fatal(err)
		}

		individualRecipients = append(individualRecipients, individualRecipient)
	}

	return individualRecipients
}
