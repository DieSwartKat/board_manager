import trello
from board_manager.settings import TRELLO_API_KEY, TRELLO_API_TOKEN, TRELLO_SUPER_USER
from rest_framework import viewsets, mixins
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from member_tracker.models import Board, Member, Board_Member_Role, Role


class RefreshData(viewsets.GenericViewSet, mixins.CreateModelMixin):
    authentication_classes = [BaseAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    trello_manager_connection = None

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.trello_manager_connection = trello.TrelloApi(
            TRELLO_API_KEY,
            TRELLO_API_TOKEN
        )

        self.super_member = self.trello_manager_connection.members.get(TRELLO_SUPER_USER)
        self.default_role = Role.objects.filter(role='member').first()
        self.get_trello_boards()


    def get_trello_boards(self):
        for board_id in self.super_member['idBoards']:
            board_object = self.save_boards(board_id)
            member_object_list = self.save_members(board_id)
            
            self.board_member_roles(board_object, member_object_list)
            

    def board_member_roles(self, board_object, member_object_list):
        for member_object in member_object_list:
            existing_links = Board_Member_Role.objects.filter(member=member_object, board=board_object).first()
            
            if not existing_links:
                print(f'Creating Link between {board_object.board_name} and {member_object.trello_username}')
                new_link = Board_Member_Role(board=board_object, member=member_object)
                new_link.save()



    def save_members(self, board_id):
        board_members = self.trello_manager_connection.boards.get_member(board_id)
        members_list = []

        for member in board_members:
            existing_member = Member.objects.filter(trello_member_id=member['id']).first()

            if not existing_member:
                fullname = member['fullName']
                print(f'Adding New Member {fullname}')

                new_member = Member(
                    trello_member_id=member['id'],
                    trello_username=member['username'],
                    )
                existing_member = new_member.save()
            if existing_member:
                members_list.append(existing_member)
        return members_list


    def save_boards(self, board_id):
        board_object = self.trello_manager_connection.boards.get(board_id)
        existing_board = Board.objects.filter(board_id=board_id).first()

        print(board_object['name'])

        if not existing_board:
            resave_board_name = Board(board_id=board_object['id'], board_name=board_object['name'])
            resave_board_name.save()
            return resave_board_name

        else:
            return existing_board

        


    