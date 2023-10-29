import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from gyms.models import *
from customers.models import *


class TrainingType(DjangoObjectType):
    class Meta:
        model = Training
        fields = ('id', 'training_type', 'price', 'gym')


class GymType(DjangoObjectType):
    class Meta:
        model = Gym
        fields = ('id', 'gym_name', 'administrator_name', 'administrator_phone', 'free_slots')


class GymInput(graphene.InputObjectType):
    gym_name = graphene.String()
    administrator_name = graphene.String()
    administrator_phone = graphene.String()
    free_slots = graphene.Int()


class PurchaseType(DjangoObjectType):
    class Meta:
        model = Purchase
        fields = ('id', 'training', 'customer', 'training_price', 'gym_income')
        filter_fields = {
            'customer__id': ('exact',),
        }
        interfaces = (graphene.relay.Node,)


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email')


class CreateGym(graphene.Mutation):
    class Arguments:
        gym_name = graphene.String()
        administrator_name = graphene.String()
        administrator_phone = graphene.String()
        free_slots = graphene.Int()

    gym = graphene.Field(GymType)

    @classmethod
    def mutate(cls, root, info, gym_name, administrator_name, administrator_phone, free_slots):
        gym = Gym(gym_name=gym_name, administrator_name=administrator_name, administrator_phone=administrator_phone,
                  free_slots=free_slots)
        gym.save()

        return CreateGym(gym=gym)


class UpdateGym(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        gym_name = graphene.String()
        administrator_name = graphene.String()
        administrator_phone = graphene.String()
        free_slots = graphene.Int()

    gym = graphene.Field(GymType)

    @classmethod
    def mutate(cls, root, info, id, gym_name=None, administrator_name=None, administrator_phone=None, free_slots=None):
        gym = Gym.objects.get(pk=id)
        gym.gym_name = gym_name if gym_name is not None else gym.gym_name
        gym.administrator_name = administrator_name if administrator_name is not None else gym.administrator_name
        gym.administrator_phone = administrator_phone if administrator_phone is not None else gym.administrator_phone
        gym.free_slots = free_slots if free_slots is not None else gym.free_slots
        gym.save()

        return UpdateGym(gym=gym)


class DeleteGym(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    gym = graphene.Field(GymType)

    @classmethod
    def mutate(self, root, info, id):
        gym = Gym.objects.get(pk=id)

        if gym is not None:
            gym.delete()

        return DeleteGym(gym=gym)


class CreateTraining(graphene.Mutation):
    class Arguments:
        training_type = graphene.String()
        price = graphene.Int()
        gym_id = graphene.Int()

    training = graphene.Field(TrainingType)

    @classmethod
    def mutate(cls, root, info, training_type, price, gym_id):
        training = Training(training_type=training_type, price=price, gym_id=gym_id)
        training.save()

        return CreateTraining(training=training)


class UpdateTraining(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        training_type = graphene.String()
        price = graphene.Int()
        gym_id = graphene.Int()

    gym = graphene.Field(GymType)

    @classmethod
    def mutate(cls, root, info, id, training_type=None, price=None, gym_id=None):
        training = Training.objects.get(pk=id)
        training.training_type = training_type if training_type is not None else training.training_type
        training.price = price if price is not None else training.price
        training.gym_id = gym_id if gym_id is not None else training.gym_id
        training.save()

        return UpdateTraining(training=training)


class DeleteTraining(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    training = graphene.Field(TrainingType)

    @classmethod
    def mutate(self, root, info, id):
        training = Training.objects.get(pk=id)

        if training is not None:
            training.delete()

        return DeleteTraining(training=training)


class CreateCustomer(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        email = graphene.String()

    customer = graphene.Field(CustomerType)

    @classmethod
    def mutate(cls, root, info, name, email):
        customer = Customer(name=name, email=email)
        customer.save()

        return CreateCustomer(customer=customer)


class UpdateCustomer(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        email = graphene.String()

    customer = graphene.Field(CustomerType)

    @classmethod
    def mutate(cls, root, info, id, name=None, email=None):
        customer = Customer.objects.get(pk=id)
        customer.name = name if name is not None else customer.name
        customer.email = email if email is not None else customer.email
        customer.save()

        return UpdateCustomer(customer=customer)


class DeleteCustomer(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    customer = graphene.Field(CustomerType)

    @classmethod
    def mutate(self, root, info, id):
        customer = Customer.objects.get(pk=id)

        if customer is not None:
            customer.delete()

        return DeleteCustomer(customer=customer)


class CreatePurchase(graphene.Mutation):
    class Arguments:
        training_id = graphene.Int()
        customer_id = graphene.Int()

    purchase = graphene.Field(PurchaseType)

    @classmethod
    def mutate(cls, root, info, training_id, customer_id):
        training = Training.objects.get(id=training_id)
        purchase = Purchase(training_id=training_id, customer_id=customer_id, training_price=training.price,
                            gym_income=training.price * 0.8)
        purchase.save()

        return CreatePurchase(purchase=purchase)


class UpdatePurchase(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        training = graphene.Int()
        customer = graphene.Int()
        training_price = graphene.Int()
        gym_income = graphene.Int()

    purchase = graphene.Field(PurchaseType)

    @classmethod
    def mutate(cls, root, info, id, training_id=None, customer_id=None, training_price=None, gym_income=None):
        purchase = Purchase.objects.get(pk=id)
        purchase.training = training_id if training_id is not None else purchase.training_id
        purchase.customer = customer_id if customer_id is not None else purchase.customer_id
        purchase.training_price = training_price if training_price is not None else purchase.training_price
        purchase.gym_income = gym_income if gym_income is not None else purchase.gym_income
        purchase.save()

        return UpdatePurchase(purchase=purchase)


class DeletePurchase(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    purchase = graphene.Field(PurchaseType)

    @classmethod
    def mutate(self, root, info, id):
        purchase = Purchase.objects.get(pk=id)

        if Purchase is not None:
            Purchase.delete()

        return DeletePurchase(purchase=purchase)


class Mutation(graphene.ObjectType):
    create_gym = CreateGym.Field()
    create_training = CreateTraining.Field()
    create_customer = CreateCustomer.Field()
    create_purchase = CreatePurchase.Field()

    update_gym = UpdateGym.Field()
    update_training = UpdateTraining.Field()
    update_customer = UpdateCustomer.Field()
    update_purchase = UpdatePurchase.Field()

    delete_gym = DeleteGym.Field()
    delete_training = DeleteTraining.Field()
    delete_customer = DeleteCustomer.Field()
    delete_purchase = DeletePurchase.Field()


class Query(graphene.ObjectType):
    all_gym = graphene.List(GymType)
    all_trainings = graphene.List(TrainingType)
    all_customers = graphene.List(CustomerType)
    customer_purchases = DjangoFilterConnectionField(PurchaseType)

    gym = graphene.Field(GymType, id=graphene.Int())
    training = graphene.Field(TrainingType, id=graphene.Int())
    customer = graphene.Field(CustomerType, id=graphene.Int())
    purchase = graphene.Field(PurchaseType, id=graphene.Int())

    def resolve_all_gym(root, info):
        return Gym.objects.all()

    def resolve_all_trainings(root, info):
        return Training.objects.all()

    def resolve_all_customers(root, info):
        return Customer.objects.all()

    def resolve_all_purchases(root, info):
        return Purchase.objects.all()

    def resolve_gym(root, info, id):
        return Gym.objects.get(id=id)

    def resolve_training(root, info, id):
        return Training.objects.get(id=id)

    def resolve_customer(root, info, id):
        return Customer.objects.get(id=id)

    def resolve_purchase(root, info, id):
        return Purchase.objects.get(id=id)


schema = graphene.Schema(query=Query, mutation=Mutation)
