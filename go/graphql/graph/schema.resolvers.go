package graph

// This file will be automatically regenerated based on the schema, any resolver implementations
// will be copied through when generating and any unknown code will be moved to the end.

import (
	"context"

	"github.com/arpan-ghosh/graphql/graph/database"
	"github.com/arpan-ghosh/graphql/graph/generated"
	"github.com/arpan-ghosh/graphql/graph/model"
)

func (r *mutationResolver) CreateIndividualContributor(ctx context.Context, input *model.NewIndividualContributor) (*model.IndividualContributor, error) {
	return db.SaveIndividualContributor(input), nil
}

func (r *mutationResolver) CreateIndividualRecipient(ctx context.Context, input *model.NewIndividualRecipient) (*model.IndividualRecipient, error) {
	return db.SaveIndividualRecipient(input), nil
}

func (r *queryResolver) IndividualContributor(ctx context.Context, id string) (*model.IndividualContributor, error) {
	return db.FindContributorByID(id), nil
}

func (r *queryResolver) IndividualContributors(ctx context.Context) ([]*model.IndividualContributor, error) {
	return db.ContributorAll(), nil
}

func (r *queryResolver) IndividualRecipient(ctx context.Context, firstName string) (*model.IndividualRecipient, error) {
	return db.FindRecipientByFirstName(firstName), nil
}

func (r *queryResolver) IndividualRecipients(ctx context.Context) ([]*model.IndividualRecipient, error) {
	return db.RecipientAll(), nil
}

// Mutation returns generated.MutationResolver implementation.
func (r *Resolver) Mutation() generated.MutationResolver { return &mutationResolver{r} }

// Query returns generated.QueryResolver implementation.
func (r *Resolver) Query() generated.QueryResolver { return &queryResolver{r} }

type mutationResolver struct{ *Resolver }
type queryResolver struct{ *Resolver }

// !!! WARNING !!!
// The code below was going to be deleted when updating resolvers. It has been copied here so you have
// one last chance to move it out of harms way if you want. There are two reasons this happens:
//  - When renaming or deleting a resolver the old code will be put in here. You can safely delete
//    it when you're done.
//  - You have helper methods in this file. Move them out to keep these resolver files clean.
var db = database.Connect()
